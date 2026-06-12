from reports.findings import FINDINGS


def vulnerability_prioritization():

    print("\n" + "=" * 50)
    print("LIPAS VULNERABILITY PRIORITIZATION")
    print("=" * 50 + "\n")

    critical = []
    high = []
    medium = []
    low = []

    for finding in FINDINGS:

        severity = finding["severity"]

        if severity == "CRITICAL":

            critical.append(
                finding
            )

        elif severity == "HIGH":

            high.append(
                finding
            )

        elif severity == "MEDIUM":

            medium.append(
                finding
            )

        else:

            low.append(
                finding
            )

    print(
        f"Critical : {len(critical)}"
    )

    print(
        f"High     : {len(high)}"
    )

    print(
        f"Medium   : {len(medium)}"
    )

    print(
        f"Low      : {len(low)}"
    )

    print("\nTop Priorities:\n")

    for finding in critical + high:

        print(
            f"[{finding['severity']}] "
            f"{finding['title']}"
        )
