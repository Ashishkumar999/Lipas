from database.finding_db import (
    add_finding_to_db
)

from models.finding_status import (
    STATUS_OPEN
)

from core.asset_manager import (
    load_assets,
    save_assets,
    update_risk_score
)


def add_finding(

    target,

    title,

    severity,

    owasp,

    cvss,

    impact,

    remediation

):

    finding = {

        "target": target,

        "title": title,

        "severity": severity,

        "owasp": owasp,

        "cvss": cvss,

        "impact": impact,

        "remediation": remediation,

        "status": STATUS_OPEN

    }

    add_finding_to_db(
        finding
    )

    assets = load_assets()

    for asset in assets:

        if asset["target"] == target:

            asset["findings"].append(
                title
            )

    save_assets(
        assets
    )

    update_risk_score(
        target
    )
