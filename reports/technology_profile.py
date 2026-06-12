from scanner.banner_fingerprint import (
    FINGERPRINT_RESULTS
)

from scanner.service_detector import (
    SERVICE_RESULTS
)


TECH_PROFILE = []


def technology_profile():

    print("\n" + "=" * 50)
    print("LIPAS TECHNOLOGY PROFILE")
    print("=" * 50 + "\n")

    technologies = set()

    for item in FINGERPRINT_RESULTS:

        technologies.add(
            item
        )

    for item in SERVICE_RESULTS:

        technologies.add(
            item
        )

    if not technologies:

        print(
            "No technology data available."
        )

        return

    TECH_PROFILE.clear()

    TECH_PROFILE.extend(
        technologies
    )

    print(
        "Detected Technologies:\n"
    )

    for tech in sorted(
        technologies
    ):

        print(
            f"[+] {tech}"
        )

    print(
        f"\nTotal Technologies: "
        f"{len(technologies)}"
    )
