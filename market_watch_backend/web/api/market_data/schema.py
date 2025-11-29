from typing import Literal

from pydantic import BaseModel


class AssetDataRequest(BaseModel):
    """Asset data request model."""

    ticker: str
    period: Literal[
        "1d",
        "5d",
        "1mo",
        "3mo",
        "6mo",
        "1y",
        "2y",
        "5y",
        "10y",
        "ytd",
        "max",
    ]
    interval: Literal[
        "1m",
        "2m",
        "5m",
        "15m",
        "30m",
        "1h",
        "1d",
        "5d",
        "1wk",
        "1mo",
        "3mo",
    ]


class AssetDataResponse(BaseModel):
    """Simple message model."""

    details: AssetDataRequest
    data: str  # JSON string representing the DataFrame


class AssetBrief(BaseModel):
    """Asset brief model."""

    ticker: str
    name: str
    current_price: float
    logo_url: str


class AllAssetsBriefResponse(BaseModel):
    """All assets brief response model."""

    stocks: list[AssetBrief]
    etfs: list[AssetBrief]
    commodities: list[AssetBrief]
    crypto: list[AssetBrief]
