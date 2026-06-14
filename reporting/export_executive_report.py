from reports.finding_db import (
    load_findings
)

from intelligence.risk_score_v2 import (
    calculate_risk_score
)


def export_executive_report():

    findings = load_findings()

    risk_score = calculate_risk_score()

    filename = (
        "reports/executive_report.txt"
    )

    with open(
        filename,
        "w"
    ) as file:

        file.write(
            "LIPAS EXECUTIVE REPORT\n\n"
        )

        file.write(
            f"Risk Score: "
            f"{risk_score}/100\n"
        )

        file.write(
            f"Total Findings: "
            f"{len(findings)}\n\n"
        )

        for item in findings:

            file.write(
                f"{item['severity']} - "
                f"{item['title']}\n"
            )

    print(
        f"Saved: {filename}"
    )
