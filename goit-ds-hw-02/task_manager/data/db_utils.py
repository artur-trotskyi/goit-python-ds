from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).resolve().parents[1] / "data" / "task_manager.db"


def execute_query(sql: str, params: tuple = ()) -> list:
    """
    Executes a SELECT query and returns the result.
    :param sql: SQL query as a string.
    :param params: Parameters to pass into the query.
    :return: A list of query results.
    """
    if not DB_PATH.exists():
        raise FileNotFoundError(f"Database not found at: {DB_PATH}")

    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()
        cur.execute(sql, params)
        return cur.fetchall()


def execute_write(sql: str, params: tuple = ()) -> int:
    """
    Executes an INSERT, UPDATE, or DELETE query and commits the changes.
    :param sql: SQL query as a string.
    :param params: Parameters to pass into the query.
    :return: The number of rows affected by the query.
    """
    if not DB_PATH.exists():
        raise FileNotFoundError(f"Database not found at: {DB_PATH}")

    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()
        cur.execute(sql, params)
        con.commit()  # Commit the changes to the database
        return cur.rowcount
