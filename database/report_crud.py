from database.sqlite_manager import (
    get_connection
)


def insert_report(

    target,

    filename

):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(

        """

        INSERT INTO reports(

            target,

            filename

        )

        VALUES(

            ?,

            ?

        )

        """,

        (

            target,

            filename

        )

    )

    conn.commit()

    conn.close()


def get_reports():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(

        "SELECT * FROM reports"

    )

    data = cursor.fetchall()

    conn.close()

    return data
