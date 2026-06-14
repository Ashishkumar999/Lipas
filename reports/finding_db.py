import json


DB_FILE = (
    "data/findings.json"
)


def load_findings():

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


def save_findings(

    findings

):

    with open(
        DB_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(

            findings,

            file,

            indent=4
        )


def add_to_database(

    finding

):

    findings = load_findings()

    findings.append(
        finding
    )

    save_findings(
        findings
    )
