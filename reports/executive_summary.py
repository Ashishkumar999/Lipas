from reports.findings import FINDINGS


def executive_summary():

    print("\n" + "=" * 50)
    print("LIPAS EXECUTIVE SUMMARY")
    print("=" * 50 + "\n")

    total = len(FINDINGS)

    high = 0
    medium = 0
    low = 0

    for finding in FINDINGS:

        severity = (
            finding["severity"]
        )

        if severity == "HIGH":

            high += 1

        elif severity == "MEDIUM":

            medium += 1

        else:

            low += 1

    print(
        f"Total Findings : {total}"
    )

    print(
        f"High Risk      : {high}"
    )

    print(
        f"Medium Risk    : {medium}"
    )

    print(
        f"Low Risk       : {low}"
    )

    print("\nOverall Assessment:")

    if high > 0:

        print(
            "Immediate remediation recommended."
        )

    elif medium > 0:

        print(
            "Moderate security improvements recommended."
        )

    else:

        print(
            "Security posture appears acceptable."
        )
