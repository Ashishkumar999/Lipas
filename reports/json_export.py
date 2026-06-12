import json

from reports.findings import FINDINGS


def export_findings_json():

    print("\n" + "=" * 50)
    print("LIPAS JSON EXPORT")
    print("=" * 50 + "\n")

    try:

        with open(
            "reports/output/findings.json",
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                FINDINGS,
                file,
                indent=4
            )

        print(
            "Export Successful."
        )

        print(
            "Saved as reports/output/findings.json"
        )

    except Exception as e:

        print(
            f"Error: {e}"
        )
