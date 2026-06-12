import requests

from reports.findings import (
    add_finding
)


def cors_analyzer():

    print("\n" + "=" * 50)
    print("LIPAS CORS ANALYZER")
    print("=" * 50 + "\n")

    url = input(
        "Enter URL: "
    ).strip()

    try:

        response = requests.get(
            url,
            timeout=10
        )

        origin = response.headers.get(
            "Access-Control-Allow-Origin"
        )

        credentials = response.headers.get(
            "Access-Control-Allow-Credentials"
        )

        if origin:

            print(
                f"Access-Control-Allow-Origin: {origin}"
            )

            if origin == "*":

                print(
                    "[WARNING] Wildcard Origin Detected"
                )

                add_finding(

                    "HIGH",

                    "Wildcard CORS Policy",

                    "Restrict allowed origins"
                )

        else:

            print(
                "No Access-Control-Allow-Origin Header"
            )

        if credentials:

            print(
                f"Access-Control-Allow-Credentials: {credentials}"
            )

            if credentials.lower() == "true":

                print(
                    "[INFO] Credentials Allowed"
                )

        else:

            print(
                "No Access-Control-Allow-Credentials Header"
            )

    except Exception as e:

        print(
            f"Error: {e}"
        )
