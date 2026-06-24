import sqlite3

DATABASE_NAME = "security_copilot.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():

    connection = get_connection()

    with open("database/schema.sql", "r") as file:
        connection.executescript(file.read())

    connection.commit()
    connection.close()