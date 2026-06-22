from database.finding_crud import (
    insert_finding,
    get_findings
)


def add_finding(

    target,

    title,

    severity

):

    insert_finding(

        target,

        title,

        severity

    )


def load_findings():

    data = get_findings()

    findings = []

    for row in data:

        findings.append(

            {

                "id": row[0],

                "target": row[1],

                "title": row[2],

                "severity": row[3]

            }

        )

    return findings
