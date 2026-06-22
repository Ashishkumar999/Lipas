from database.finding_crud import (

    insert_finding,

    get_findings

)


class FindingRepository:

    def create(

        self,

        target,

        title,

        severity

    ):

        insert_finding(

            target,

            title,

            severity

        )

    def all(

        self

    ):

        return get_findings()
