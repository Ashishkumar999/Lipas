import requests

from reports.findings import (
    add_finding
)


def robots_analyzer():

    print("\n" + "=" * 50)
    print("LIPAS ROBOTS.TXT ANALYZER")
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

    robots_url = (
        f"{target}/robots.txt"
    )

    try:

        response = requests.get(
            robots_url,
            timeout=10
        )

        if response.status_code != 200:

            print(
                "robots.txt not found."
            )

            return

        print(
            f"Found: {robots_url}\n"
        )

        lines = response.text.split(
            "\n"
        )

        discovered = 0

        for line in lines:

            line = line.strip()

            if line.startswith(
                "Disallow:"
            ):

                path = line.replace(
                    "Disallow:",
                    ""
                ).strip()

                discovered += 1

                print(
                    f"[PATH] {path}"
                )

                add_finding(

                    "LOW",

                    f"Robots.txt Disclosed Path ({path})",

                    "Review exposed directories"
                )

        print(
            f"\nTotal Paths: {discovered}"
        )

    except Exception as e:

        print(
            f"Error: {e}"
        )
