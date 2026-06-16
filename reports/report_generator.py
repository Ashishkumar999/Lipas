import re
from datetime import datetime

from scanner.port_scanner import OPEN_PORTS
from scanner.tech_detector import TECH_RESULTS
from scanner.dir_discovery import FOUND_DIRS
from recon.subdomain_enum import FOUND_SUBDOMAINS


def generate_report(target):

    filename = re.sub(
        r"[^a-zA-Z0-9_-]",
        "_",
        target
    )

    report_file = (
        f"reports/{filename}_report.txt"
    )

    with open(
        report_file,
        "w",
        encoding="utf-8"
    ) as report:

        report.write(
            "=====================================\n"
        )

        report.write(
            "LIPAS VAPT REPORT\n"
        )

        report.write(
            "=====================================\n\n"
        )

        report.write(
            f"Target : {target}\n"
        )

        report.write(
            f"Date   : {datetime.now()}\n\n"
        )

        report.write(
            "OPEN PORTS\n"
        )

        report.write(
            "----------\n"
        )

        for port in OPEN_PORTS:

            report.write(
                f"Port {port}\n"
            )

        report.write("\n")

        report.write(
            "TECHNOLOGIES\n"
        )

        report.write(
            "------------\n"
        )

        for tech in TECH_RESULTS:

            report.write(
                f"{tech}\n"
            )

        report.write("\n")

        report.write(
            "DIRECTORIES\n"
        )

        report.write(
            "-----------\n"
        )

        for item in FOUND_DIRS:

            report.write(
                f"{item}\n"
            )

        report.write("\n")

        report.write(
            "SUBDOMAINS\n"
        )

        report.write(
            "----------\n"
        )

        for sub in FOUND_SUBDOMAINS:

            report.write(
                f"{sub}\n"
            )

    print(
        f"\n[+] Report Saved: {report_file}"
    )
