import requests

from reports.findings import (
    add_finding
)


PARAMETERS = [

    "id",

    "user",

    "admin",

    "debug",

    "token",

    "redirect",

    "file",

    "url",

    "page",

    "search"
]


def parameter_finder():

    print("\n" + "=" * 50)
    print("LIPAS HIDDEN PARAMETER FINDER")
    print("=" * 50 + "\n")

    target = input(
        "Enter Target URL: "
    ).strip()

    if not target.startswith(
        "http"
    ):

        target = (
            "https://" + target
        )

    discovered = 0

    for param in PARAMETERS:

        try:

            url = (
                f"{target}?{param}=test"
            )

            response = requests.get(
                url,
                timeout=5
            )

            if response.status_code in [
                200,
                302,
                403
            ]:

                discovered += 1

                print(
                    f"[POSSIBLE] {param}"
                )

        except:

            pass

    print(
        f"\nParameters Identified: "
        f"{discovered}"
    )

    if discovered > 0:

        add_finding(

            "LOW",

            "Potential Hidden Parameters Found",

            "Review identified parameters manually"
        )
