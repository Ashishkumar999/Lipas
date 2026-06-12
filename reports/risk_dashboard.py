from scanner.security_headers import HEADER_RESULTS


def risk_dashboard():

    print("\n" + "=" * 50)
    print("LIPAS RISK DASHBOARD")
    print("=" * 50 + "\n")

    high = []
    medium = []
    low = []

    for item in HEADER_RESULTS:

        if "Content-Security-Policy" in item:

            if "[MISSING]" in item:

                high.append(
                    "Missing CSP Header"
                )

        elif "Strict-Transport-Security" in item:

            if "[MISSING]" in item:

                medium.append(
                    "Missing HSTS Header"
                )

        elif "[MISSING]" in item:

            low.append(item)

    print("HIGH RISK")
    print("-" * 20)

    for item in high:

        print(item)

    print("\nMEDIUM RISK")
    print("-" * 20)

    for item in medium:

        print(item)

    print("\nLOW RISK")
    print("-" * 20)

    for item in low:

        print(item)

    score = 100

    score -= len(high) * 15
    score -= len(medium) * 10
    score -= len(low) * 5

    if score < 0:

        score = 0

    print("\n" + "=" * 50)

    print(
        f"Overall Security Score: {score}/100"
    )
