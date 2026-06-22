from database.sqlite_manager import (
    get_connection
)


def insert_asset(

    target,

    risk_score=0

):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(

        """

        INSERT INTO assets(

            target,

            risk_score

        )

        VALUES(

            ?,

            ?

        )

        """,

        (

            target,

            risk_score

        )

    )

    conn.commit()

    conn.close()


def get_assets():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(

        "SELECT * FROM assets"

    )

    data = cursor.fetchall()

    conn.close()

    return data


def delete_asset(

    asset_id

):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(

        """

        DELETE FROM assets

        WHERE id=?

        """,

        (

            asset_id,

        )

    )

    conn.commit()

    conn.close()
