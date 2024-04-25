import chromadb
from fastapi import UploadFile
from app.api.v1.on_disk.service import EmbeddingService
from app.core.utils import base_response_to_json_response
from .schemas.requests import EmbedOnlineFileRequest
from typing import Dict


class EmbeddingView:
    def __init__(self, embed_service: EmbeddingService = EmbeddingService()):
        self.embed_service = embed_service

    async def embed_local(self, file: UploadFile, collection: str):
        try:
            await self.embed_service.embedLocal(file=file, collection=collection)
        except Exception as e:
            return base_response_to_json_response(e)

    async def embed_persistent(self, embed_request: EmbedOnlineFileRequest):
        try:
            await self.embed_service.embedRemote(embed_request)
        except Exception as e:
            print("Error---->", e)
            return base_response_to_json_response(e)

    def get_all_collections(self):
        persistent_client = chromadb.PersistentClient()
        return persistent_client.list_collections()

    def add_to_collection(self, collection_name: str, items: Dict[str, str]):
        persistent_client = chromadb.PersistentClient()
        self.embed_service.add_to_collection(persistent_client, collection_name, items)

    def get_single_collection(self, collection_name: str):
        persistent_client = chromadb.PersistentClient()
        return self.embed_service.get_single_collection(
            persistent_client, collection_name
        )
