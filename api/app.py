from fastapi import FastAPI

from api.routes.assets import (
    router as assets_router
)

from api.routes.findings import (
    router as findings_router
)

from api.routes.dashboard import (
    router as dashboard_router
)

from api.routes.reports import (
    router as reports_router
)
from api.routes.web import (
    router as web_router
)


app = FastAPI(

    title="LIPAS Enterprise API"

)

app.include_router(
    assets_router
)

app.include_router(
    findings_router
)

app.include_router(
    dashboard_router
)

app.include_router(
    reports_router
)

app.include_router(
    web_router
)
