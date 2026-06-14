from models.finding import (
    Finding
)

from intelligence.owasp_mapper import (
    map_owasp
)

from intelligence.risk_engine import (
    calculate_cvss
)


FINDINGS_V2 = []

FINDING_COUNTER = 1


def add_finding_v2(

    severity,

    title,

    remediation,

    asset="Unknown"

):

    global FINDING_COUNTER

    finding = Finding(

        f"LIPAS-{FINDING_COUNTER:03}",

        title,

        severity,

        map_owasp(title),

        calculate_cvss(severity),

        "Impact analysis pending",

        remediation,

        asset

    )

    FINDINGS_V2.append(

        finding.to_dict()
    )

    FINDING_COUNTER += 1
