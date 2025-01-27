from random import randint
import faker

from task_manager.data.db_utils import execute_query, execute_write

STATUSES = ['new', 'in progress', 'completed']


def get_user_tasks(user_id: int) -> list:
    """
    Retrieves all tasks for a given user based on their user_id.
    :param user_id: The user's ID.
    :return: A list of tasks for the user.
    """
    sql = """
        SELECT * FROM tasks
        WHERE user_id = ?;
    """

    return execute_query(sql, (user_id,))


def get_tasks_by_status(status_name: str, except_status: bool = False) -> list:
    """
    Retrieves tasks based on their status.
    If `except_status` is True, retrieves all tasks except those with the specified status.
    :param status_name: The name of the status to filter tasks by.
    :param except_status: A boolean flag to exclude tasks with the given status (default is False).
    :return: A list of tasks matching the given criteria.
    """
    if except_status:
        sql = """
            SELECT * FROM tasks
            WHERE status_id != (SELECT id FROM status WHERE name = ?);
        """
    else:
        sql = """
            SELECT * FROM tasks
            WHERE status_id = (SELECT id FROM status WHERE name = ?);
        """
    return execute_query(sql, (status_name,))


def get_tasks_by_user_email(email: str) -> list:
    """
    Fetches tasks for users matching the given email.
    :param email: The email to search for.
    :return: A list of tasks associated with the user having the given email.
    """
    sql = """
        SELECT tasks.*
        FROM tasks
        JOIN users ON tasks.user_id = users.id
        WHERE users.email LIKE ?;
    """

    return execute_query(sql, (f"%{email}",))


def get_task_count_by_status() -> list:
    """
    Fetches the count of tasks grouped by their status.
    :return: A list of tuples where each tuple contains the status name and the count of tasks.
    """
    sql = """
        SELECT status.name, COUNT(tasks.id) 
        FROM tasks
        LEFT JOIN status ON status.id = tasks.status_id
        GROUP BY status.name;
    """

    return execute_query(sql, ())


def get_tasks_without_description() -> list:
    """
    Retrieves a list of tasks that do not have a description.
    :return: A list of tasks without a description.
    """
    sql = """
        SELECT * FROM tasks
        WHERE description IS NULL OR description = '';
    """

    return execute_query(sql, ())


def update_task_status(status_name: str, task_id: int) -> int:
    """
    Updates the status of a task based on the provided task ID and status name.
    :param status_name: The name of the new status (string).
    :param task_id: The ID of the task to be updated (integer).
    :return: An integer representing the number of rows affected by the query.
             Returns 1 if the task was updated successfully, 0 if no rows were affected.
    """
    sql_get_status_id = """
        SELECT id FROM status WHERE name = ?;
    """
    status = execute_query(sql_get_status_id, (status_name,))
    status_id = status[0][0] if status else None
    if not status_id:
        return 0

    sql_update_task = """
        UPDATE tasks
        SET status_id = ?
        WHERE id = ?
    """

    return execute_write(sql_update_task, (status_id, task_id))


def add_task(task_data: tuple) -> int:
    """
    Adds a new task to the tasks table in the database.
    :param task_data: A tuple containing the task's title, description, status ID, and user ID.
    :return: An integer representing the number of rows affected by the query.
             Returns 1 if the task was added successfully, 0 if no rows were affected.
    """
    sql = """
        INSERT INTO tasks (title, description, status_id, user_id)
        VALUES (?, ?, ?, ?);
    """

    return execute_write(sql, task_data)


def delete_task(task_id: int) -> int:
    """
    Deletes a task from the tasks table in the database.
    :param task_id: The ID of the task to be deleted.
    :return: An integer representing the number of rows affected by the query.
             Returns 1 if the task was deleted successfully, 0 if no rows were affected.
    """
    sql = """
        DELETE FROM tasks 
        WHERE id = ?;
    """

    return execute_write(sql, (task_id,))


def generate_fake_task(user_id: int) -> tuple:
    """
    Generates fake task data for testing purposes.
    :param user_id: The user ID to associate the task with.
    :return: A tuple containing fake task data: title, description, status ID, and user ID.
    """
    fake_data = faker.Faker('uk_UA')

    return (
        fake_data.sentence(nb_words=5),
        fake_data.paragraph(nb_sentences=3),
        randint(1, len(STATUSES)),
        user_id
    )


def print_tasks(tasks: list) -> None:
    """
    Prints the list of tasks.
    :param tasks: A list of tasks to display.
    :return: None
    """
    if not tasks:
        print("No tasks available.")
        print('\n')
        return

    print("Tasks:")
    for task in tasks:
        print(task)

    print('\n')


def print_task_result(rows: int, action: str) -> None:
    """
    Prints a message about the result of a task-related operation.
    :param rows: The number of rows affected by the operation.
    :param action: The type of action performed (e.g., 'updated', 'added', 'deleted').
    :return: None
    """
    action = action.lower()
    if action not in {"updated", "added", "deleted"}:
        raise ValueError("Action must be one of: 'updated', 'added', 'deleted'.")

    print(f"{rows} task(s) have been {action}." if rows > 0 else f"No task(s) were {action}.")
    print('\n')
