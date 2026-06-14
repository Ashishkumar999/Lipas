from models.finding import (
    Finding
)

from intelligence.owasp_mapper import (
    map_owasp
)

from intelligence.risk_engine import (
    calculate_cvss
)

from reports.finding_db import (
    add_to_database
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

        map_owasp(
            title
        ),

        calculate_cvss(
            severity
        ),

        "Impact analysis pending",

        remediation,

        asset
    )

    data = finding.to_dict()

    FINDINGS_V2.append(
        data
    )

    add_to_database(
        data
    )

    FINDING_COUNTER += 1


def show_findings_v2():

    print("\n" + "=" * 50)
    print("LIPAS ENTERPRISE FINDINGS")
    print("=" * 50 + "\n")

    if not FINDINGS_V2:

        print(
            "No findings available."
        )

        return

    for finding in FINDINGS_V2:

        print(
            f"ID: {finding['id']}"
        )

        print(
            f"Title: {finding['title']}"
        )

        print(
            f"Severity: "
            f"{finding['severity']}"
        )

        print(
            f"OWASP: "
            f"{finding['owasp']}"
        )

        print(
            f"CVSS: "
            f"{finding['cvss']}"
        )

        print(
            f"Asset: "
            f"{finding['asset']}"
        )

        print(
            "-" * 50
        )
