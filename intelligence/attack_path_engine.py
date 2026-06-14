from reports.finding_db import (
    load_findings
)

from intelligence.attack_paths import (
    ATTACK_PATHS
)

from intelligence.attack_priority import (
    attack_priority
)


def attack_path_engine():

    print("\n" + "=" * 60)
    print("LIPAS ATTACK PATH ANALYSIS")
    print("=" * 60 + "\n")

    findings = load_findings()

    if not findings:

        print(
            "No findings available."
        )

        return

    for finding in findings:

        title = finding.get(
            "title",
            ""
        )

        severity = finding.get(
            "severity",
            "LOW"
        )

        print(
            f"Finding: {title}"
        )

        print(
            f"Priority: {attack_priority(severity)}"
        )

        path_found = False

        for key in ATTACK_PATHS:

            if key.lower() in title.lower():

                path_found = True

                print(
                    "\nPotential Attack Path:\n"
                )

                steps = ATTACK_PATHS[key]

                for step in steps:

                    print(step)

                    if step != steps[-1]:

                        print("↓")

        if not path_found:

            print(
                "No attack path available."
            )

        print(
            "\n" + "-" * 60 + "\n"
        )
