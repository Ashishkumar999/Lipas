from core.asset_manager import (
    load_assets,
    save_assets
)


def add_tag(

    target,

    tag

):

    assets = load_assets()

    for asset in assets:

        if asset["target"] == target:

            if "tags" not in asset:

                asset["tags"] = []

            if tag not in asset["tags"]:

                asset["tags"].append(
                    tag
                )

    save_assets(
        assets
    )
