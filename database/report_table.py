from database.sqlite_manager import (
    get_connection
)


def create_report_table():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(

        """

        CREATE TABLE IF NOT EXISTS reports(

            id INTEGER PRIMARY KEY,

            target TEXT,

            filename TEXT

        )

        """

    )

    conn.commit()

    conn.close()
