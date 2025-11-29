import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import lru_cache
from pathlib import Path

from market_watch_backend.settings import ASSETS_FILE
from market_watch_backend.web.api.market_data.repository import fetch_asset_brief
from market_watch_backend.web.api.market_data.schema import (
    AllAssetsBriefResponse,
)


@lru_cache
def load_assets_json() -> dict[str, list[dict[str, str]]]:
    """
    Load assets from JSON file.

    :returns: dictionary with available assets.
    """
    with Path.open(ASSETS_FILE, "r") as f:
        return json.load(f)


def get_all_assets_brief() -> AllAssetsBriefResponse:
    """
    Get a brief list of all available financial assets.

    :returns: a brief list of assets.
    """
    available_assets = load_assets_json()

    all_asset_data = AllAssetsBriefResponse(
        stocks=[],
        etfs=[],
        commodities=[],
        crypto=[],
    )

    if not available_assets:
        return all_asset_data

    for category, values in available_assets.items():
        # Use ThreadPoolExecutor to fetch asset briefs concurrently
        with ThreadPoolExecutor(max_workers=len(values)) as executor:
            futures = [
                executor.submit(
                    fetch_asset_brief,
                    ticker=asset["ticker"],
                    logo_url=asset["logoUrl"],
                )
                for asset in values
            ]

            for future in as_completed(futures):
                try:
                    asset_brief = future.result()
                    getattr(all_asset_data, category).append(asset_brief)
                except Exception as e:
                    # Handle exceptions if needed
                    raise e

    return all_asset_data
