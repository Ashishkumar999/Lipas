import json
from datetime import datetime

from core.target_manager import (
    get_target
)

from core.asset_manager import (
    get_asset
)

from database.finding_db import (
    load_findings
)


def generate_txt():

    target = get_target()

    if not target:

        print(
            "\n[-] No target selected"
        )

        return

    asset = get_asset(
        target
    )

    if not asset:

        print(
            "\n[-] Asset not found"
        )

        return

    findings = load_findings()

    filename = (

        "reports/"

        +

        target.replace(
            ".",
            "_"
        )

        +

        ".txt"

    )

    with open(

        filename,

        "w",

        encoding="utf-8"

    ) as report:

        report.write(
            "LIPAS ENTERPRISE REPORT\n"
        )

        report.write(
            "=" * 50
            +
            "\n"
        )

        report.write(
            f"Target: {target}\n"
        )

        report.write(
            f"Generated: {datetime.now()}\n\n"
        )

        report.write(
            "OPEN PORTS\n"
        )

        report.write(
            "-" * 20
            +
            "\n"
        )

        for port in asset.get(
            "ports",
            []
        ):

            report.write(
                f"{port}\n"
            )

        report.write(
            "\nSERVICES\n"
        )

        report.write(
            "-" * 20
            +
            "\n"
        )

        for service in asset.get(
            "services",
            []
        ):

            report.write(
                f"{service}\n"
            )

        report.write(
            "\nFINDINGS\n"
        )

        report.write(
            "-" * 20
            +
            "\n"
        )

        for finding in findings:

            if finding["target"] == target:

                report.write(

                    f'{finding["severity"]} | '

                    f'{finding["title"]}\n'

                )

    print(
        f"\n[+] TXT Report Saved: {filename}"
    )


def generate_json():

    target = get_target()

    if not target:

        print(
            "\n[-] No target selected"
        )

        return

    asset = get_asset(
        target
    )

    if not asset:

        print(
            "\n[-] Asset not found"
        )

        return

    filename = (

        "reports/"

        +

        target.replace(
            ".",
            "_"
        )

        +

        ".json"

    )

    with open(

        filename,

        "w",

        encoding="utf-8"

    ) as file:

        json.dump(

            asset,

            file,

            indent=4

        )

    print(
        f"\n[+] JSON Report Saved: {filename}"
    )
