from reports.finding_db import (
    load_findings
)


def database_viewer():

    print("\n" + "=" * 50)
    print("LIPAS FINDING DATABASE")
    print("=" * 50 + "\n")

    findings = load_findings()

    if not findings:

        print(
            "No findings stored."
        )

        return

    for item in findings:

        print(
            f"ID: {item['id']}"
        )

        print(
            f"Title: {item['title']}"
        )

        print(
            f"Severity: "
            f"{item['severity']}"
        )

        print(
            f"OWASP: "
            f"{item['owasp']}"
        )

        print(
            "-" * 50
        )
