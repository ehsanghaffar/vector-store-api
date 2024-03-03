from enum import Enum

from pydantic import BaseModel, Field




class EmbedOnlineFileRequest(BaseModel):
    file_url: str = Field(..., description="File URL")
    collection_name: str = Field(..., description="Name of collection")
