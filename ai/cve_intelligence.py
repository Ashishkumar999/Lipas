from database.cve_database import (
    load_cves
)


def cve_intelligence():

    cves = load_cves()

    print()

    print(
        "CVE Intelligence"
    )

    print()

    print(

        "Known CVEs :",

        len(
            cves
        )

    )
