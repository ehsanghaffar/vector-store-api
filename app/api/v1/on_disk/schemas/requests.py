from enum import Enum

from fastapi import UploadFile
from pydantic import BaseModel, Field




class EmbedOnlineFileRequest(BaseModel):
    file_url: str = Field(..., description="File URL")
    collection_name: str = Field(..., description="Name of collection")


class EmbedOfflineFileRequest(BaseModel):
    file: UploadFile = Field(..., description="File")
    collection_name: str = Field(..., description="Name of collection")