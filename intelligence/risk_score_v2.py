from reports.finding_db import (
    load_findings
)


def calculate_risk_score():

    findings = load_findings()

    if not findings:

        return 0

    score = 0

    for item in findings:

        severity = item.get(
            "severity",
            ""
        )

        if severity == "CRITICAL":

            score += 25

        elif severity == "HIGH":

            score += 20

        elif severity == "MEDIUM":

            score += 10

        elif severity == "LOW":

            score += 3

    if score > 100:

        score = 100

    return score
