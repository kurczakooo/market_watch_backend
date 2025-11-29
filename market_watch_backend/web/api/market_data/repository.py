import yfinance as yf

from market_watch_backend.web.api.market_data.schema import (
    AssetBrief,
    AssetDataRequest,
    AssetDataResponse,
)


def fetch_single_asset_specific_data(
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


def fetch_asset_brief(ticker: str, logo_url: str) -> AssetBrief:
    """
    Fetch brief information for a single asset.

    :param ticker: Asset ticker symbol.
    :param logo_url: URL to the asset's logo.
    :returns: AssetBrief object.
    """
    t = yf.Ticker(ticker).get_info()

    name = t.get("longName") or t.get("shortName") or ticker
    current_price = t.get("regularMarketPrice", 0.0)

    return AssetBrief(
        ticker=ticker,
        name=name,
        current_price=current_price,
        logo_url=logo_url,
    )
