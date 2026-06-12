import requests


FINGERPRINT_RESULTS = []


def banner_fingerprint(target):

    print("\n" + "=" * 50)
    print("LIPAS BANNER FINGERPRINT")
    print("=" * 50 + "\n")

    if not target.startswith(
        "http"
    ):

        target = (
            "https://" + target
        )

    try:

        response = requests.get(
            target,
            timeout=5
        )

        server = response.headers.get(
            "Server"
        )

        powered_by = response.headers.get(
            "X-Powered-By"
        )

        FINGERPRINT_RESULTS.clear()

        if server:

            print(
                f"Server: {server}"
            )

            FINGERPRINT_RESULTS.append(
                server
            )

        if powered_by:

            print(
                f"X-Powered-By: {powered_by}"
            )

            FINGERPRINT_RESULTS.append(
                powered_by
            )

        if not server and not powered_by:

            print(
                "No fingerprint data found."
            )

    except Exception as e:

        print(
            f"Error: {e}"
        )
