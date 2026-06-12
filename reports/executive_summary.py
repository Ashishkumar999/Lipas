from reports.findings import FINDINGS


SUMMARY_RESULTS = {}


def executive_summary():

    print("\n" + "=" * 50)
    print("LIPAS EXECUTIVE SUMMARY")
    print("=" * 50 + "\n")

    total = len(FINDINGS)

    high = 0
    medium = 0
    low = 0

    for finding in FINDINGS:

        severity = finding["severity"]

        if severity == "HIGH":

            high += 1

        elif severity == "MEDIUM":

            medium += 1

        else:

            low += 1

    SUMMARY_RESULTS["total"] = total
    SUMMARY_RESULTS["high"] = high
    SUMMARY_RESULTS["medium"] = medium
    SUMMARY_RESULTS["low"] = low

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

    print("\nOverall Assessment:\n")

    if high > 0:

        print(
            "Immediate remediation recommended."
        )

    elif medium > 0:

        print(
            "Moderate security improvements recommended."
        )

    elif low > 0:

        print(
            "Minor security improvements recommended."
        )

    else:

        print(
            "No significant findings detected."
        )

    print("\n" + "=" * 50)
