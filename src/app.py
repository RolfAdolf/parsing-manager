import logging

from fastapi import FastAPI
from routers.base import base_router


logger = logging.getLogger(__name__)


def create_app() -> FastAPI:
    """Фабрика приложения"""
    app_ = FastAPI()
    app_.include_router(base_router)

    return app_


app = create_app()
