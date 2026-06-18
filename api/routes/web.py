from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi import Request

from core.asset_manager import (
    load_assets
)

router = APIRouter()

templates = Jinja2Templates(

    directory="web/templates"

)


@router.get("/")
def home(

    request: Request

):

    assets = load_assets()

    return templates.TemplateResponse(

        request,

        "dashboard.html",

        {

            "assets": len(

                assets

            )

        }

    )
