from database.sqlite_manager import (
    get_connection
)


def create_asset_table():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(

        """

        CREATE TABLE IF NOT EXISTS assets(

            id INTEGER PRIMARY KEY,

            target TEXT,

            risk_score INTEGER

        )

        """

    )

    conn.commit()

    conn.close()
