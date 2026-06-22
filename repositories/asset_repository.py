from database.asset_crud import (

    insert_asset,

    get_assets

)


class AssetRepository:

    def create(

        self,

        target,

        risk_score=0

    ):

        insert_asset(

            target,

            risk_score

        )

    def all(

        self

    ):

        return get_assets()
