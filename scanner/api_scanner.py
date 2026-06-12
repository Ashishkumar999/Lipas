import requests


def api_scanner():

    print("\n" + "=" * 50)
    print("LIPAS API SECURITY SCANNER")
    print("=" * 50 + "\n")

    url = input(
        "Enter API URL: "
    ).strip()

    try:

        response = requests.get(
            url,
            timeout=10
        )

        print(
            f"Status Code: {response.status_code}"
        )

        print(
            f"Server: "
            f"{response.headers.get('Server', 'Unknown')}"
        )

        print(
            f"Content-Type: "
            f"{response.headers.get('Content-Type', 'Unknown')}"
        )

        print("\nSecurity Headers:\n")

        headers = [

            "Content-Security-Policy",

            "Strict-Transport-Security",

            "X-Frame-Options",

            "X-Content-Type-Options"
        ]

        for header in headers:

            if header in response.headers:

                print(
                    f"[FOUND] {header}"
                )

            else:

                print(
                    f"[MISSING] {header}"
                )

    except Exception as e:

        print(
            f"Error: {e}"
        )
