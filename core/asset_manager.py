from database.asset_crud import (
    insert_asset,
    get_assets
)


def create_asset(

    target

):

    assets = get_assets()

    for asset in assets:

        if asset[1] == target:

            return

    insert_asset(

        target,

        0

    )


def load_assets():

    data = get_assets()

    assets = []

    for row in data:

        assets.append(

            {

                "id": row[0],

                "target": row[1],

                "risk_score": row[2]

            }

        )

    return assets
