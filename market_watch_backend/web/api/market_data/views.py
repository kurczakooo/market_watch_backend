from fastapi import APIRouter

from market_watch_backend.web.api.market_data.repository import (
    fetch_single_asset_specific_data,
)
from market_watch_backend.web.api.market_data.schema import (
    AllAssetsBriefResponse,
    AssetDataRequest,
    AssetDataResponse,
)
from market_watch_backend.web.api.market_data.service import get_all_assets_brief

router = APIRouter()


@router.post("/", response_model=AssetDataResponse)
async def get_single_asset_specific_data(
    request: AssetDataRequest,
) -> AssetDataResponse:
    """
    Get single financial asset data, with specified period and interval.

    :param request: asset data request.
    :returns: asset data response (A json DataFrame).
    """
    return fetch_single_asset_specific_data(request=request)


@router.get("/all-assets-brief")
async def get_assets_brief() -> AllAssetsBriefResponse:
    """
    Get a brief list of available financial assets.

    :returns: a brief list of assets.
    """

    # For demonstration purposes, we return a static list.
    return get_all_assets_brief()
