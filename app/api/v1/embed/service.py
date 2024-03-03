import os
import shutil
from langchain_community.document_loaders import (
    CSVLoader,
    EverNoteLoader,
    PDFMinerLoader,
    TextLoader,
    UnstructuredEPubLoader,
    UnstructuredHTMLLoader,
    UnstructuredMarkdownLoader,
    UnstructuredODTLoader,
    UnstructuredPowerPointLoader,
    UnstructuredWordDocumentLoader,
    NotebookLoader,
)
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.api.v1.embed.schemas.requests import EmbedOnlineFileRequest
from app.core.config import get_settings
from app.core.utils import download_file
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores.chroma import Chroma

CHROMA_PATH = "chroma"
DATA_PATH = "data/books"

# Map file extensions to document loaders and their arguments
LOADER_MAPPING = {
    ".html": (UnstructuredHTMLLoader, {}),
    ".pdf": (PDFMinerLoader, {}),
    ".pptx": (UnstructuredPowerPointLoader, {}),
    ".md": (UnstructuredMarkdownLoader, {}),
    ".ipynb": (NotebookLoader, {}),
    ".csv": (CSVLoader, {"encoding": "utf8"}),
    ".doc": (UnstructuredWordDocumentLoader, {}),
    ".docx": (UnstructuredWordDocumentLoader, {}),
    ".enex": (EverNoteLoader, {}),
    ".epub": (UnstructuredEPubLoader, {}),
    ".odt": (UnstructuredODTLoader, {}),
    ".ppt": (UnstructuredPowerPointLoader, {}),
    ".txt": (TextLoader, {"encoding": "utf8"}),
}

def load_documents_from_url(file_url: str, tmp_path: str = "tmp"):

    file_path = download_file(url=file_url, save_path=tmp_path)

    ext = "." + file_path.rsplit(".", 1)[-1]
    if ext in LOADER_MAPPING:
        loader_class, loader_args = LOADER_MAPPING[ext]
        loader = loader_class(file_path, **loader_args)
        return loader.load()

    raise ValueError(f"Unsupported file extension '{ext}'")




def split_text(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

    document = chunks[10]
    print(document.page_content)
    print(document.metadata)

    return chunks

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")


def save_to_chroma(chunks: list[Document], chroma_path: str, collection: str):
    # Clear out the database first.
    if os.path.exists(chroma_path):
        shutil.rmtree(chroma_path)

    # Create a new DB from the documents.
    db = Chroma.from_documents(
        documents=chunks, embedding=embeddings, persist_directory=chroma_path, collection_name=collection
    )
    db.persist()
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")


class EmbeddingService:
    def __init__(self):
        self.settings = get_settings()

    async def embedRemote(self, embed_request: EmbedOnlineFileRequest):
        loaded_file = load_documents_from_url(file_url=embed_request.file_url)
        documents = split_text(loaded_file)
        save_to_chroma(chunks=documents, chroma_path=self.settings.CHROMA_PATH, collection=embed_request.collection_name)