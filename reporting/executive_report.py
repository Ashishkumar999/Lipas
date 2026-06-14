from reports.finding_db import (
    load_findings
)

from intelligence.risk_score_v2 import (
    calculate_risk_score
)


def executive_report():

    print("\n" + "=" * 60)
    print("LIPAS EXECUTIVE SECURITY REPORT")
    print("=" * 60 + "\n")

    findings = load_findings()

    risk_score = calculate_risk_score()

    if risk_score >= 80:

        rating = "CRITICAL"

    elif risk_score >= 60:

        rating = "HIGH"

    elif risk_score >= 40:

        rating = "MEDIUM"

    else:

        rating = "LOW"

    print(
        f"Overall Risk Score : {risk_score}/100"
    )

    print(
        f"Risk Rating        : {rating}"
    )

    print(
        f"Total Findings     : {len(findings)}"
    )

    print("\n" + "-" * 60)

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

    print("\nFINDING SUMMARY\n")

    print(f"HIGH   : {high}")
    print(f"MEDIUM : {medium}")
    print(f"LOW    : {low}")

    print("\nTOP RISKS\n")

    for finding in findings[:5]:

        print(
            f"- {finding['title']}"
        )

    print("\nBUSINESS IMPACT\n")

    if high > 0:

        print(
            "- Potential account compromise"
        )

        print(
            "- Data exposure risk"
        )

        print(
            "- Regulatory compliance impact"
        )

    else:

        print(
            "- No major business risks identified"
        )

    print("\nREMEDIATION PRIORITY\n")

    print(
        "1. Fix HIGH findings"
    )

    print(
        "2. Address MEDIUM findings"
    )

    print(
        "3. Review LOW findings"
    )

    print(
        "\nAssessment Completed."
    )
