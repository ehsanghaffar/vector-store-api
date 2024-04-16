from fastapi import APIRouter
from app.core.config import get_settings

from .on_disk.routes import embed_router as embed_v1_router
settings = get_settings()

router = APIRouter()

router.include_router(embed_v1_router, prefix=settings.API_V1_PREFIX + "/embed", tags=["Embedding"])

__all__ = ["router"]