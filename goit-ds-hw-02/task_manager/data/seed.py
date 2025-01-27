from pathlib import Path
from random import randint
import faker
import sqlite3

STATUSES = ['new', 'in progress', 'completed']
DB_PATH = Path(__file__).resolve().parent / "task_manager.db"


def generate_fake_data(number_users: int, number_tasks: int) -> tuple:
    """
    Generates fake data for users, statuses, and tasks.
    :param number_users: The number of fake users to generate.
    :param number_tasks: The number of fake tasks to generate.
    :return: A tuple containing lists of fake users, statuses, and tasks.
    """
    fake_data = faker.Faker('uk_UA')

    # Generate fake users
    fake_users = []
    seen_emails = set()  # Track seen emails to ensure uniqueness
    for user_id in range(1, number_users + 1):
        while True:
            email = fake_data.email()  # Generate a fake email
            if email not in seen_emails:  # Ensure email is unique
                seen_emails.add(email)
                fake_users.append((user_id, fake_data.name(), email))  # Append user data (id, name, email)
                break

    # Generate task statuses (new, in progress, completed)
    fake_statuses = [(status_id, status_name) for status_id, status_name in enumerate(STATUSES, start=1)]

    # Generate fake tasks with random user IDs and status IDs
    number_statuses = len(fake_statuses)
    fake_tasks = [
        (
            task_id,
            fake_data.sentence(nb_words=5),  # Generate a fake task title
            fake_data.paragraph(nb_sentences=3) if randint(0, 10) < 10 else '',  # Generate a fake task description
            randint(1, number_statuses),  # Random status ID
            randint(2, number_users)  # Random user ID (user_id = 1 doesn't have a task)
        )
        for task_id in range(1, number_tasks + 1)
    ]

    return fake_users, fake_statuses, fake_tasks


def insert_data_to_db(users: list[tuple], statuses: list[tuple], tasks: list[tuple]) -> None:
    """
    Inserts the generated fake data into the database.
    :param users: List of users to be inserted.
    :param statuses: List of statuses to be inserted.
    :param tasks: List of tasks to be inserted.
    :return: None
    """
    # Connect to the SQLite database
    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()

        # Clear existing data from the tables
        cur.execute("DELETE FROM tasks")
        cur.execute("DELETE FROM status")
        cur.execute("DELETE FROM users")

        # Insert users into the users table
        sql_to_users = """INSERT INTO users(id, fullname, email) VALUES (?, ?, ?)"""
        cur.executemany(sql_to_users, users)

        # Insert statuses into the statuses table
        sql_to_statuses = """INSERT INTO status(id, name) VALUES (?, ?)"""
        cur.executemany(sql_to_statuses, statuses)

        # Insert tasks into the tasks table in batches
        sql_to_tasks = """INSERT INTO tasks(id, title, description, status_id, user_id) VALUES (?, ?, ?, ?, ?)"""
        tasks_count = len(tasks)
        batch_size = max(500, tasks_count // 10)
        for i in range(0, tasks_count, batch_size):
            cur.executemany(sql_to_tasks, tasks[i:i + batch_size])

        con.commit()
