from fastapi import APIRouter

from database.finding_db import (
    load_findings
)

router = APIRouter()


@router.get(
    "/findings"
)
def findings():

    return load_findings()
