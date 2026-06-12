import re
import requests

from reports.findings import (
    add_finding
)


def js_intelligence():

    print("\n" + "=" * 50)
    print("LIPAS JAVASCRIPT INTELLIGENCE")
    print("=" * 50 + "\n")

    url = input(
        "Enter JavaScript URL: "
    ).strip()

    try:

        response = requests.get(
            url,
            timeout=10
        )

        content = response.text

        print(
            "\nScanning JavaScript...\n"
        )

        urls = re.findall(

            r'https?://[^\s"\']+',

            content
        )

        endpoints = re.findall(

            r'/[a-zA-Z0-9_\-/]+',

            content
        )

        print(
            f"URLs Found: {len(urls)}"
        )

        for item in urls[:20]:

            print(
                f"[URL] {item}"
            )

        print()

        print(
            f"Endpoints Found: "
            f"{len(endpoints)}"
        )

        for item in endpoints[:20]:

            print(
                f"[ENDPOINT] {item}"
            )

        if urls:

            add_finding(

                "LOW",

                "JavaScript URLs Discovered",

                "Review exposed endpoints"
            )

    except Exception as e:

        print(
            f"Error: {e}"
        )
