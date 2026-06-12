FINDINGS = []


def add_finding(
    severity,
    title,
    recommendation
):

    FINDINGS.append({

        "severity": severity,

        "title": title,

        "recommendation":
            recommendation
    })


def show_findings():

    print("\n" + "=" * 50)
    print("LIPAS FINDING MANAGER")
    print("=" * 50)

    for i, finding in enumerate(
        FINDINGS,
        start=1
    ):

        print(
            f"\nLIPAS-{i:03}"
        )

        print(
            f"Severity: "
            f"{finding['severity']}"
        )

        print(
            f"Finding: "
            f"{finding['title']}"
        )

        print(
            f"Recommendation: "
            f"{finding['recommendation']}"
        )
