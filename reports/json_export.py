import json

from reports.findings_db import (
    FINDINGS_DB
)


def export_json(target):

    filename = (
        target.replace(".", "_")
    )

    path = (
        f"assessments/"
        f"{filename}_findings.json"
    )

    with open(path, "w") as file:

        json.dump(
            FINDINGS_DB,
            file,
            indent=4
        )

    print(
        f"Saved: {path}"
    )
