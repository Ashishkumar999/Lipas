from fastapi import APIRouter

from core.asset_manager import (
    load_assets
)

router = APIRouter()


@router.get(
    "/assets"
)
def assets():

    return load_assets()
