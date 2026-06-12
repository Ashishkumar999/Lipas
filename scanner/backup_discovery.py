import requests

from reports.findings import (
    add_finding
)


BACKUP_FILES = [

    "backup.zip",

    "backup.tar.gz",

    "website.zip",

    "site.zip",

    "www.zip",

    "db.sql",

    "database.sql",

    "index.php.bak",

    "index.php.old",

    "config.php.bak",

    "backup.rar",

    "source.zip"
]


def backup_discovery():

    print("\n" + "=" * 50)
    print("LIPAS BACKUP FILE DISCOVERY")
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

    for item in BACKUP_FILES:

        try:

            url = (
                f"{target}/{item}"
            )

            response = requests.get(
                url,
                timeout=5
            )

            if response.status_code == 200:

                discovered += 1

                print(
                    f"[FOUND] {url}"
                )

                add_finding(

                    "HIGH",

                    f"Backup File Exposed ({item})",

                    f"Remove or protect {item}"
                )

        except:

            pass

    print(
        f"\nTotal Files Found: "
        f"{discovered}"
    )
