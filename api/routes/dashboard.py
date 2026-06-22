from fastapi import APIRouter

from core.asset_manager import (
    load_assets
)

from core.findings_manager import (
    load_findings
)

router = APIRouter()


@router.get(
    "/dashboard"
)

def dashboard():

    assets = load_assets()

    findings = load_findings()

    return {

        "assets":

        len(
            assets
        ),

        "findings":

        len(
            findings
        )

    }
