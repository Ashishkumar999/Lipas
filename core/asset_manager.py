import json

from core.risk_engine import (
    calculate_risk
)

ASSET_DB = "data/assets.json"


def load_assets():

    try:

        with open(
            ASSET_DB,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(
                file
            )

    except:

        return []


def save_assets(
    assets
):

    with open(
        ASSET_DB,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            assets,
            file,
            indent=4
        )


def create_asset(
    target
):

    assets = load_assets()

    for asset in assets:

        if asset["target"] == target:

            return

    assets.append(

        {

            "target": target,

            "ip": "",

            "ports": [],

            "services": [],

            "technologies": [],

            "subdomains": [],

            "directories": [],

            "findings": [],

            "risk_score": 0,

            "last_scan": ""

        }

    )

    save_assets(
        assets
    )


def get_asset(
    target
):

    assets = load_assets()

    for asset in assets:

        if asset["target"] == target:

            return asset

    return None


def update_risk_score(
    target
):

    assets = load_assets()

    for asset in assets:

        if asset["target"] == target:

            asset["risk_score"] = (

                calculate_risk(
                    asset
                )

            )

    save_assets(
        assets
    )


def add_port(
    target,
    port
):

    assets = load_assets()

    for asset in assets:

        if asset["target"] == target:

            if port not in asset["ports"]:

                asset["ports"].append(
                    port
                )

    save_assets(
        assets
    )

    update_risk_score(
        target
    )


def add_service(
    target,
    service
):

    assets = load_assets()

    for asset in assets:

        if asset["target"] == target:

            if service not in asset["services"]:

                asset["services"].append(
                    service
                )

    save_assets(
        assets
    )

    update_risk_score(
        target
    )


def add_technology(
    target,
    technology
):

    assets = load_assets()

    for asset in assets:

        if asset["target"] == target:

            if technology not in asset["technologies"]:

                asset["technologies"].append(
                    technology
                )

    save_assets(
        assets
    )

    update_risk_score(
        target
    )


def add_subdomain(
    target,
    subdomain
):

    assets = load_assets()

    for asset in assets:

        if asset["target"] == target:

            if subdomain not in asset["subdomains"]:

                asset["subdomains"].append(
                    subdomain
                )

    save_assets(
        assets
    )


def add_directory(
    target,
    directory
):

    assets = load_assets()

    for asset in assets:

        if asset["target"] == target:

            if directory not in asset["directories"]:

                asset["directories"].append(
                    directory
                )

    save_assets(
        assets
    )


def show_asset_details(
    target
):

    return get_asset(
        target
    )
