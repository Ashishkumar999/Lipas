import requests

from reports.findings import (
    add_finding
)

HEADER_RESULTS = []


def security_headers_check(target):

    print("\n" + "=" * 50)
    print("LIPAS SECURITY HEADERS")
    print("=" * 50 + "\n")

    if not target.startswith(
        "http"
    ):

        target = (
            "https://" + target
        )

    headers_to_check = [

        "Content-Security-Policy",

        "Strict-Transport-Security",

        "X-Frame-Options",

        "X-Content-Type-Options",

        "Referrer-Policy"
    ]

    try:

        response = requests.get(
            target,
            timeout=5
        )

        for header in headers_to_check:

            if header in response.headers:

                result = (
                    f"[FOUND] {header}"
                )

                print(result)

                HEADER_RESULTS.append(
                    result
                )

            else:

                result = (
                    f"[MISSING] {header}"
                )

                print(result)

                HEADER_RESULTS.append(
                    result
                )

                severity = "LOW"

                if header == (
                    "Content-Security-Policy"
                ):

                    severity = "HIGH"

                elif header == (
                    "Strict-Transport-Security"
                ):

                    severity = "MEDIUM"

                add_finding(

                    severity,

                    f"Missing {header}",

                    f"Implement {header}"
                )

    except Exception as e:

        print(
            f"Error: {e}"
        )
