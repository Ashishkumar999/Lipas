from reports.findings import (
    FINDINGS
)

from reports.asset_correlation import (
    ASSET_RESULTS
)

from reports.technology_profile import (
    TECH_PROFILE
)


def attack_surface_report():

    print("\n" + "=" * 50)
    print("LIPAS ATTACK SURFACE INTELLIGENCE")
    print("=" * 50 + "\n")

    print(
        f"Assets: "
        f"{len(ASSET_RESULTS)}"
    )

    print(
        f"Technologies: "
        f"{len(TECH_PROFILE)}"
    )

    print(
        f"Findings: "
        f"{len(FINDINGS)}"
    )

    print("\nRisk Overview\n")

    high = 0
    medium = 0
    low = 0

    for finding in FINDINGS:

        severity = finding.get(
            "severity",
            ""
        )

        if severity == "HIGH":

            high += 1

        elif severity == "MEDIUM":

            medium += 1

        elif severity == "LOW":

            low += 1

    print(
        f"HIGH   : {high}"
    )

    print(
        f"MEDIUM : {medium}"
    )

    print(
        f"LOW    : {low}"
    )

    print("\nTechnology Stack\n")

    if TECH_PROFILE:

        for tech in TECH_PROFILE:

            print(
                f"[+] {tech}"
            )

    else:

        print(
            "No technologies discovered."
        )

    print("\nAssessment Complete")
