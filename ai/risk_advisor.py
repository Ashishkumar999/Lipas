from reports.findings import FINDINGS


def risk_advisor():

    print("\n" + "=" * 50)
    print("LIPAS AI RISK ADVISOR")
    print("=" * 50 + "\n")

    if not FINDINGS:

        print(
            "No findings available."
        )

        return

    for finding in FINDINGS:

        title = finding["title"]

        severity = finding["severity"]

        print(
            f"\nFinding: {title}"
        )

        print(
            f"Severity: {severity}"
        )

        if (
            "Content-Security-Policy"
            in title
        ):

            print(
                "\nImpact:"
            )

            print(
                "May allow XSS attacks."
            )

            print(
                "\nRecommendation:"
            )

            print(
                "Implement CSP header."
            )

        elif (
            "Strict-Transport-Security"
            in title
        ):

            print(
                "\nImpact:"
            )

            print(
                "HTTPS downgrade attacks may be possible."
            )

            print(
                "\nRecommendation:"
            )

            print(
                "Enable HSTS."
            )

        else:

            print(
                "\nImpact:"
            )

            print(
                "Security weakness detected."
            )

            print(
                "\nRecommendation:"
            )

            print(
                finding[
                    "recommendation"
                ]
            )

        print(
            "\n" + "-" * 40
        )
