from fastapi.routing import APIRouter

from market_watch_backend.web.api import market_data, monitoring

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(
    market_data.router,
    prefix="/market_data",
    tags=["market_data"],
)
