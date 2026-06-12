import requests

from reports.findings import (
    add_finding
)


SENSITIVE_FILES = [

    ".env",

    ".git/config",

    "backup.zip",

    "backup.tar.gz",

    "database.sql",

    "db.sql",

    "config.php.bak",

    "config.bak",

    "web.config",

    ".htaccess",

    "admin.zip"
]


def sensitive_file_discovery():

    print("\n" + "=" * 50)
    print("LIPAS SENSITIVE FILE DISCOVERY")
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

    found = 0

    for item in SENSITIVE_FILES:

        try:

            url = (
                f"{target}/{item}"
            )

            response = requests.get(
                url,
                timeout=5
            )

            if response.status_code == 200:

                found += 1

                print(
                    f"[FOUND] {url}"
                )

                add_finding(

                    "HIGH",

                    f"Sensitive File Exposed ({item})",

                    f"Restrict access to {item}"
                )

        except:

            pass

    print(
        f"\nTotal Found: {found}"
    )
