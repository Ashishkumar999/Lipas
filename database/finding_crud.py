from database.sqlite_manager import (
    get_connection
)


def insert_finding(

    target,

    title,

    severity

):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(

        """

        INSERT INTO findings(

            target,

            title,

            severity

        )

        VALUES(

            ?,

            ?,

            ?

        )

        """,

        (

            target,

            title,

            severity

        )

    )

    conn.commit()

    conn.close()


def get_findings():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(

        "SELECT * FROM findings"

    )

    data = cursor.fetchall()

    conn.close()

    return data
