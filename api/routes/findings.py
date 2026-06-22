from fastapi import APIRouter

from core.findings_manager import (
    load_findings
)

router = APIRouter()


@router.get(

    "/findings"

)

def findings():

    return load_findings()
