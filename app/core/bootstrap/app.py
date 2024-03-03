from fastapi import FastAPI

from app.core.config import Settings, get_settings

from .middlewares import init_middlewares
from .routers import init_routers
from .handlers import init_handlers


def create_app() -> FastAPI:
    settings: Settings = get_settings()

    app_ = FastAPI(
        title=settings.PROJECT_TITLE,
        description=settings.PROJECT_DESCRIPTION,
        version=settings.PROJECT_VERSION,
        docs_url=None if settings.ENV == "prod" else "/docs",
        redoc_url=None if settings.ENV == "prod" else "/redoc",
    )

    # Initializing required dependencies
    init_handlers(app_=app_)
    init_middlewares(app_=app_)
    init_routers(app_=app_)

    return app_
