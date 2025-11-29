from importlib import metadata

from fastapi import FastAPI
from fastapi.responses import UJSONResponse
from fastapi.staticfiles import StaticFiles

from market_watch_backend.settings import STATIC_DIR
from market_watch_backend.web.api.router import api_router
from market_watch_backend.web.lifespan import lifespan_setup


def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """
    app = FastAPI(
        title="market_watch_backend",
        version=metadata.version("market_watch_backend"),
        lifespan=lifespan_setup,
        docs_url="/api/docs",
        redoc_url="/api/redoc",
        openapi_url="/api/openapi.json",
        default_response_class=UJSONResponse,
    )

    # Main router for the API.
    app.include_router(router=api_router, prefix="/api")

    # Mount static files (mock blob storage).
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

    return app
