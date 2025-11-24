import yfinance as yf
from fastapi import APIRouter

from market_watch_backend.web.api.market_data.schema import (
    AssetDataRequest,
    AssetDataResponse,
)

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
    df = yf.download(
        tickers=request.ticker,
        period=request.period,
        interval=request.interval,
    )

    # Convert DataFrame to JSON
    df_json = df.reset_index().to_json()

    return AssetDataResponse(details=request, data=df_json)
