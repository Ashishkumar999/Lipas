import json


ASSET_DB = "data/assets.json"



def show_asset_details(
    target
):

    asset = get_asset(
        target
    )

    if not asset:

        return None

    return asset


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


def save_assets(assets):

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


def create_asset(target):

    assets = load_assets()

    for asset in assets:

        if asset["target"] == target:

            return

    assets.append({

        "target": target,

        "ports": [],

        "services": [],

        "technologies": [],

        "findings": [],

        "risk_score": 0

    })

    save_assets(
        assets
    )


def get_asset(target):

    assets = load_assets()

    for asset in assets:

        if asset["target"] == target:

            return asset

    return None


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
