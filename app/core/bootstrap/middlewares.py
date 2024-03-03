from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import Settings, get_settings
from app.core.middlewares.logging import LoggingMiddleware
from app.core.middlewares.request_id import RequestIdMiddleware


def init_middlewares(app_: FastAPI) -> None:
    settings: Settings = get_settings()

    app_.add_middleware(LoggingMiddleware)
    app_.add_middleware(RequestIdMiddleware)

    # CORSMiddleware
    app_.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )