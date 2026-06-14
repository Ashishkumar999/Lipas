from reports.findings_v2 import (
    FINDINGS_V2
)

from intelligence.enrichment import (
    enrich_finding
)


def intelligence_viewer():

    print("\n" + "=" * 50)
    print("LIPAS OWASP INTELLIGENCE")
    print("=" * 50 + "\n")

    if not FINDINGS_V2:

        print(
            "No findings available."
        )

        return

    for finding in FINDINGS_V2:

        data = enrich_finding(
            finding
        )

        print(
            f"ID: {data['id']}"
        )

        print(
            f"Title: {data['title']}"
        )

        print(
            f"Severity: {data['severity']}"
        )

        print(
            f"OWASP: "
            f"{data.get('owasp_name','Unknown')}"
        )

        print(
            f"CVSS: {data['cvss']}"
        )

        print(
            f"Attack Scenario:"
        )

        print(
            data.get(
                "attack_scenario",
                "N/A"
            )
        )

        print(
            f"Business Impact:"
        )

        print(
            data.get(
                "business_impact",
                "N/A"
            )
        )

        print(
            f"Reference:"
        )

        print(
            data.get(
                "reference",
                "N/A"
            )
        )

        print(
            "-" * 50
        )
