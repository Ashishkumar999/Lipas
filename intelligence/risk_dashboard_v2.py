from reports.finding_db import (
    load_findings
)

from intelligence.risk_score_v2 import (
    calculate_risk_score
)


def risk_dashboard_v2():

    print("\n" + "=" * 50)
    print("LIPAS ENTERPRISE RISK DASHBOARD")
    print("=" * 50 + "\n")

    findings = load_findings()

    score = calculate_risk_score()

    print(
        f"Overall Risk Score: "
        f"{score}/100"
    )

    if score >= 80:

        rating = "CRITICAL"

    elif score >= 60:

        rating = "HIGH"

    elif score >= 40:

        rating = "MEDIUM"

    else:

        rating = "LOW"

    print(
        f"Risk Rating: "
        f"{rating}"
    )

    print(
        f"Total Findings: "
        f"{len(findings)}"
    )

    high = 0
    medium = 0
    low = 0

    for item in findings:

        severity = item.get(
            "severity",
            ""
        )

        if severity == "HIGH":

            high += 1

        elif severity == "MEDIUM":

            medium += 1

        elif severity == "LOW":

            low += 1

    print("\nBreakdown\n")

    print(
        f"HIGH   : {high}"
    )

    print(
        f"MEDIUM : {medium}"
    )

    print(
        f"LOW    : {low}"
    )
