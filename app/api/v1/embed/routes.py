from fastapi import APIRouter

from app.api.v1.embed.schemas.exceptions import ValidationErrorResponse
from app.api.v1.embed.schemas.responses import EmbedFileSuccessfully
from app.api.v1.embed.view import EmbeddingView

embed_view = EmbeddingView()

embed_router = APIRouter(
    responses={
        # 404: {"description": "Not found", "model": UserNotFound},
        422: {"description": "Validation Error", "model": ValidationErrorResponse},
    },

)

embed_router.add_api_route(
    "/remote",
    embed_view.embedRemote,
    description="Embedding online docs",
    methods=["POST"],
    response_model=EmbedFileSuccessfully,
    status_code=EmbedFileSuccessfully().status_code,
)