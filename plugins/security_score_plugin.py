from database.finding_db import load_findings
from core.target_manager import get_target
from core.ui import banner


def run():

    target = get_target()

    banner(
        "SECURITY SCORE"
    )

    score = 100

    findings = load_findings()

    count = 0

    for finding in findings:

        if finding["target"] == target:

            count += 1

    score -= count * 5

    if score < 0:

        score = 0

    print()

    print(
        f"Security Score : {score}/100"
    )

    if score >= 90:

        print(
            "Excellent 🟢"
        )

    elif score >= 70:

        print(
            "Good 🟡"
        )

    elif score >= 50:

        print(
            "Moderate 🟠"
        )

    else:

        print(
            "Weak 🔴"
        )
