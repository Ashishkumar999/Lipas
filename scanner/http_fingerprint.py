import requests


def http_fingerprint(target):

    print("\nHTTP Fingerprint\n")

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
            "Server",
            "Unknown"
        )

        powered = response.headers.get(
            "X-Powered-By",
            "Unknown"
        )

        print(
            f"Server: {server}"
        )

        print(
            f"X-Powered-By: {powered}"
        )

    except Exception as e:

        print(e)
