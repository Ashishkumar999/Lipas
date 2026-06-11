HEADER_RESULTS = []

import requests


SECURITY_HEADERS = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Permissions-Policy"
]


def security_headers_check(target):

    print("\n" + "=" * 50)
    print("LIPAS SECURITY HEADERS AUDITOR")
    print("=" * 50 + "\n")

    try:

        if not target.startswith("http"):
            target = "https://" + target

        response = requests.get(
            target,
            timeout=10
        )

        headers = response.headers

        print("\nSecurity Header Results\n")

        for header in SECURITY_HEADERS:

            if header in headers:

               result = f"[FOUND] {header}"

               print(result)

               HEADER_RESULTS.append(result)

            else:

               result = f"[MISSING] {header}"

               print(result)

               HEADER_RESULTS.append(result)

    except Exception as e:

        print(
            f"Error: {e}"
        )
