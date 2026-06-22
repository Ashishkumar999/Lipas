from database.report_crud import (

    insert_report,

    get_reports

)


class ReportRepository:

    def create(

        self,

        target,

        filename

    ):

        insert_report(

            target,

            filename

        )

    def all(

        self

    ):

        return get_reports()
