from fastapi import APIRouter

from app.api.v1.on_disk.schemas.exceptions import ValidationErrorResponse
from app.api.v1.on_disk.schemas.responses import (
    EmbedFileSuccessfully,
    GetCollectionSuccessfully,
)
from app.api.v1.on_disk.view import EmbeddingView

embed_view = EmbeddingView()

embed_router = APIRouter(
    responses={
        # 404: {"description": "Not found", "model": UserNotFound},
        422: {"description": "Validation Error", "model": ValidationErrorResponse},
    },
)

embed_router.add_api_route(
    "/upload-local",
    embed_view.embed_local,
    description="Embedding local docs",
    methods=["POST"],
    # response_model=EmbedFileSuccessfully,
    status_code=EmbedFileSuccessfully().status_code,
)

embed_router.add_api_route(
    "/upload-remote",
    embed_view.embed_persistent,
    description="Embedding online docs",
    methods=["POST"],
    # response_model=EmbedFileSuccessfully,
    status_code=EmbedFileSuccessfully().status_code,
)

embed_router.add_api_route(
    "/collections",
    embed_view.get_all_collections,
    description="Get all collections",
    methods=["GET"],
    # response_model=GetCollectionSuccessfully,
    status_code=GetCollectionSuccessfully().status_code,
)

embed_router.add_api_route(
    "/add",
    embed_view.add_to_collection,
    description="Add to collection",
    methods=["POST"],
    # response_model=GetCollectionSuccessfully,
    status_code=GetCollectionSuccessfully().status_code,
)

embed_router.add_api_route(
    "/get-collection",
    embed_view.get_single_collection,
    description="Get collection",
    methods=["POST"],
    # response_model=GetCollectionSuccessfully,
    status_code=GetCollectionSuccessfully().status_code,
)
