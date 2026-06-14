from reports.finding_db import (
    load_findings
)

from intelligence.explanation_engine import (
    explain_vulnerability
)


def explanation_viewer():

    print("\n" + "=" * 50)
    print("LIPAS VULNERABILITY EXPLANATIONS")
    print("=" * 50 + "\n")

    findings = load_findings()

    if not findings:

        print(
            "No findings available."
        )

        return

    for finding in findings:

        title = finding.get(
            "title",
            ""
        )

        info = explain_vulnerability(
            title
        )

        print(
            f"Finding: {title}"
        )

        print(
            f"Severity: "
            f"{finding.get('severity')}"
        )

        print(
            "\nWhy Vulnerable:"
        )

        print(
            info["why"]
        )

        print(
            "\nAttack Scenario:"
        )

        print(
            info["attack"]
        )

        print(
            "\nImpact:"
        )

        print(
            info["impact"]
        )

        print(
            "\nRemediation:"
        )

        print(
            info["remediation"]
        )

        print(
            "\n" + "-" * 50 + "\n"
        )
