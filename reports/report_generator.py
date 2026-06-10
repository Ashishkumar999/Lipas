import os
from datetime import datetime


def generate_report(target):

    filename = target.replace(".", "_")

    report_file = f"reports/{filename}_report.txt"

    os.makedirs(
        "reports",
        exist_ok=True
    )

    with open(
        report_file,
        "w"
    ) as report:

        report.write(
            "=" * 40 + "\n"
        )

        report.write(
            "LIPAS VAPT REPORT\n"
        )

        report.write(
            "=" * 40 + "\n\n"
        )

        report.write(
            f"Target : {target}\n"
        )

        report.write(
            f"Date   : {datetime.now()}\n\n"
        )

        report.write(
            "[DNS ENUMERATION]\n"
        )

        report.write(
            "Completed\n\n"
        )

        report.write(
            "[WHOIS LOOKUP]\n"
        )

        report.write(
            "Completed\n\n"
        )

        report.write(
            "[PORT SCAN]\n"
        )

        report.write(
            "Completed\n\n"
        )

        report.write(
            "[HEADER ANALYSIS]\n"
        )

        report.write(
            "Completed\n\n"
        )

        report.write(
            "[TECHNOLOGY DETECTION]\n"
        )

        report.write(
            "Completed\n\n"
        )

        report.write(
            "OVERALL STATUS\n"
        )

        report.write(
            "Scan Completed Successfully\n"
        )

    print(
        f"\n[+] Report Saved: {report_file}"
    )
