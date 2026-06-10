import requests

SECURITY_HEADERS = {
    "Content-Security-Policy": "HIGH",
    "Strict-Transport-Security": "MEDIUM",
    "X-Frame-Options": "MEDIUM",
    "X-Content-Type-Options": "LOW",
    "Referrer-Policy": "LOW"
}


def analyze_headers(target):

    if not target.startswith("http"):
        target = "https://" + target

    try:

        response = requests.get(
            target,
            timeout=10
        )

        headers = response.headers

        print("\n" + "=" * 50)
        print("LIPAS SECURITY HEADER ANALYZER")
        print("=" * 50 + "\n")

        high = 0
        medium = 0
        low = 0

        for header, severity in SECURITY_HEADERS.items():

            if header not in headers:

                print(
                    f"[{severity}] Missing {header}"
                )

                if severity == "HIGH":
                    high += 1

                elif severity == "MEDIUM":
                    medium += 1

                else:
                    low += 1

            else:

                print(
                    f"[OK] {header}"
                )

        print("\nSUMMARY")
        print(f"HIGH   : {high}")
        print(f"MEDIUM : {medium}")
        print(f"LOW    : {low}")

    except Exception as e:

        print(f"Error: {e}")
