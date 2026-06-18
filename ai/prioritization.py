from database.finding_db import (
    load_findings
)


def prioritize():

    findings = load_findings()

    print()

    print(
        "Priority Findings"
    )

    print()

    for finding in findings:

        if finding.get(
            "severity"
        ) == "HIGH 🔴":

            print(

                "[HIGH]",

                finding.get(
                    "title"
                )

            )


def vulnerability_prioritization():

    prioritize()
