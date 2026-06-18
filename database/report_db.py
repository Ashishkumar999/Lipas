import json

DB_FILE = "database/reports.json"


def load_reports():

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


def save_reports(
    reports
):

    with open(
        DB_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            reports,
            file,
            indent=4
        )


def add_report(
    report
):

    reports = load_reports()

    reports.append(
        report
    )

    save_reports(
        reports
    )
