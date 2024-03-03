from app.api.v1.embed.service import EmbeddingService
from app.core.utils import base_response_to_json_response
from .schemas.requests import EmbedOnlineFileRequest
from .schemas.responses import EmbedFileSuccessfully


class EmbeddingView:
    def __init__(self, embed_service: EmbeddingService = EmbeddingService()):
        self.embed_service = embed_service


    async def embedRemote(self, embed_request: EmbedOnlineFileRequest):
        try:
            await self.embed_service.embedRemote(embed_request)
        except Exception as e:
          print("Error---->", e)
          return base_response_to_json_response(e)