import sqlite3


DATABASE = "database/lipas.db"


def get_connection():

    return sqlite3.connect(
        DATABASE
    )
