import base64
import json

from reports.findings import (
    add_finding
)


def jwt_analyzer():

    print("\n" + "=" * 50)
    print("LIPAS JWT ANALYZER")
    print("=" * 50 + "\n")

    token = input(
        "Enter JWT Token: "
    ).strip()

    try:

        parts = token.split(".")

        if len(parts) != 3:

            print(
                "Invalid JWT Format"
            )

            return

        header = parts[0]
        payload = parts[1]

        header += "=" * (
            -len(header) % 4
        )

        payload += "=" * (
            -len(payload) % 4
        )

        decoded_header = json.loads(

            base64.urlsafe_b64decode(
                header
            ).decode()

        )

        decoded_payload = json.loads(

            base64.urlsafe_b64decode(
                payload
            ).decode()

        )

        print("\nHEADER\n")
        print(decoded_header)

        print("\nPAYLOAD\n")
        print(decoded_payload)

        alg = decoded_header.get(
            "alg"
        )

        if alg == "none":

            print(
                "\n[HIGH] JWT Uses alg=none"
            )

            add_finding(

                "HIGH",

                "JWT Uses alg=none",

                "Use a secure signing algorithm"
            )

        else:

            print(
                f"\nAlgorithm: {alg}"
            )

    except Exception as e:

        print(
            f"Error: {e}"
        )
