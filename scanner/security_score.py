from scanner.security_headers import HEADER_RESULTS


def security_score():

    print("\n" + "=" * 50)
    print("LIPAS SECURITY SCORECARD")
    print("=" * 50 + "\n")

    score = 100

    found_headers = 0
    missing_headers = 0

    for item in HEADER_RESULTS:

        if "[FOUND]" in item:

            found_headers += 1

        elif "[MISSING]" in item:

            missing_headers += 1

    score -= (missing_headers * 5)

    print(
        f"Security Headers : {found_headers}/6"
    )

    print(
        f"Missing Headers  : {missing_headers}"
    )

    print(
        f"\nOverall Score    : {score}/100"
    )

    if score >= 90:

        risk = "LOW"

    elif score >= 70:

        risk = "MEDIUM"

    else:

        risk = "HIGH"

    print(
        f"Risk Level       : {risk}"
    )
