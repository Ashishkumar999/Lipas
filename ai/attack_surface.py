from database.finding_db import (
    load_findings
)


def attack_surface():

    findings = load_findings()

    print()

    print(
        "Attack Surface Overview"
    )

    print()

    print(

        "Total Findings:",

        len(
            findings
        )

    )


def attack_surface_report():

    attack_surface()
