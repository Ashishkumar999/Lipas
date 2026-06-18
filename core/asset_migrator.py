from core.asset_manager import (
    load_assets,
    save_assets
)


def migrate_assets():

    assets = load_assets()

    for asset in assets:

        if "ip" not in asset:

            asset["ip"] = ""

        if "subdomains" not in asset:

            asset["subdomains"] = []

        if "directories" not in asset:

            asset["directories"] = []

        if "last_scan" not in asset:

            asset["last_scan"] = ""

        if "findings" not in asset:

            asset["findings"] = []

        if "technologies" not in asset:

            asset["technologies"] = []

        if "risk_score" not in asset:

            asset["risk_score"] = 0

    save_assets(
        assets
    )

    print(
        "[+] Asset migration complete"
    )
