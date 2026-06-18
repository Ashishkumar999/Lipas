from database.finding_db import load_findings


def owasp_checker():

    findings = load_findings()

    owasp = {}

    for finding in findings:

        category = finding.get(

            "owasp",

            "Unknown"

        )

        owasp[category] = (

            owasp.get(

                category,

                0

            )

            + 1

        )

    print()

    print(

        "OWASP Distribution"

    )

    print()

    for category in owasp:

        print(

            category,

            ":",

            owasp[category]

        )
