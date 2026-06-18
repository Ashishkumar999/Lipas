import json

DB_FILE = "database/cve_db.json"


def load_cves():

    try:

        with open(
            DB_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(
                file
            )

    except:

        return []


def save_cves(
    cves
):

    with open(
        DB_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            cves,
            file,
            indent=4
        )


def add_cve(
    cve
):

    cves = load_cves()

    cves.append(
        cve
    )

    save_cves(
        cves
    )
