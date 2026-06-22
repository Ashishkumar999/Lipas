from database.sqlite_manager import (
    get_connection
)


def create_finding_table():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(

        """

        CREATE TABLE IF NOT EXISTS findings(

            id INTEGER PRIMARY KEY,

            target TEXT,

            title TEXT,

            severity TEXT

        )

        """

    )

    conn.commit()

    conn.close()
