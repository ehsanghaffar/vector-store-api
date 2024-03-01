from fastapi import APIRouter
from core.config import get_settings

# from .register.routes import register_router as register_v1_router

settings = get_settings()

router = APIRouter()
# router.include_router(register_v1_router, prefix=settings.API_V1_PREFIX + "/register", tags=["Registration"])

__all__ = ["router"]