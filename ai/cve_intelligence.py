from scanner.banner_fingerprint import (
    FINGERPRINT_RESULTS
)

from scanner.cve_lookup import (
    CVE_DATABASE
)

from reports.findings import (
    add_finding
)


def cve_intelligence():

    print("\n" + "=" * 50)
    print("LIPAS CVE INTELLIGENCE")
    print("=" * 50 + "\n")

    if not FINGERPRINT_RESULTS:

        print(
            "No fingerprint data available."
        )

        return

    matches = 0

    for software in FINGERPRINT_RESULTS:

        cves = CVE_DATABASE.get(
            software
        )

        if cves:

            matches += 1

            print(
                f"Software: {software}"
            )

            print(
                "Known CVEs:"
            )

            for cve in cves:

                print(
                    f" - {cve}"
                )

                add_finding(

                    "HIGH",

                    f"Known Vulnerability ({software})",

                    f"Review {cve}"
                )

            print()

    if matches == 0:

        print(
            "No matching CVEs found."
        )
