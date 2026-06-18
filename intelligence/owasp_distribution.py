from database.finding_db import (
    load_findings
)


def owasp_distribution():

    findings = load_findings()

    distribution = {}

    for finding in findings:

        owasp = finding["owasp"]

        distribution[owasp] = (

            distribution.get(
                owasp,
                0
            ) + 1

        )

    return distribution
