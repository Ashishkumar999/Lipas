from fastapi import APIRouter

from core.asset_manager import (
    load_assets
)

router = APIRouter()


@router.get(
    "/dashboard"
)
def dashboard():

    assets = load_assets()

    return {

        "assets":

        len(
            assets
        )

    }
