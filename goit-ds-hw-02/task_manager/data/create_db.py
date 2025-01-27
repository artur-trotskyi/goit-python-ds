import sqlite3
from pathlib import Path

SQL_PATH = Path(__file__).resolve().parent / "task_manager.sql"
DB_PATH = Path(__file__).resolve().parent / "task_manager.db"


def create_db():
    # Read the SQL script from the file to create the database schema
    with open(SQL_PATH, 'r') as f:
        sql = f.read()

    # Establish a connection to the database (if the file doesn't exist, it will be created)
    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()
        # Execute the SQL script to create tables in the database
        cur.executescript(sql)
