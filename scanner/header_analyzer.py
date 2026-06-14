import requests

from core.target_manager import (
    get_target
)


def analyze_headers():

    target = get_target()

    if not target:

        print(
            "\nNo target selected."
        )

        return

    if not target.startswith(
        "http"
    ):

        target = (
            "https://" + target
        )

    print(
        "\n" + "=" * 50
    )

    print(
        "LIPAS HEADER ANALYZER"
    )

    print(
        "=" * 50 + "\n"
    )

    try:

        response = requests.get(
            target,
            timeout=10
        )

        print(
            f"Target: {target}\n"
        )

        for header, value in (
            response.headers.items()
        ):

            print(
                f"{header}: {value}"
            )

    except Exception as e:

        print(
            f"\nError: {e}"
        )
