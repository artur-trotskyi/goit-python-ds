from task_manager.data.db_utils import execute_query, execute_write


def get_users_with_no_tasks() -> list:
    """
    Retrieves a list of users who do not have any tasks assigned.
    :return: A list of users without tasks.
    """
    sql = """
        SELECT * FROM users
        WHERE id NOT IN (
            SELECT DISTINCT user_id FROM tasks
        );
    """

    return execute_query(sql, ())


def get_users_with_tasks_by_status(status_name: str) -> list:
    """
    Retrieves a list of users along with their tasks where the task's status matches the provided status name.
    :param status_name: The status of the task to filter by (e.g., 'completed', 'in progress').
    :return: A list of users along with the tasks that match the specified status.
    """
    sql = """
        SELECT users.*, tasks.title, tasks.description, status.name
        FROM users
        INNER JOIN tasks ON tasks.user_id = users.id
        INNER JOIN status ON status.id = tasks.status_id
        WHERE status.name = ?;
    """

    return execute_query(sql, (status_name,))


def get_users_and_task_count() -> list:
    """
    Retrieves a list of users along with the count of tasks assigned to each user.
    :return: A list of tuples, each containing a user and their respective task count.
    """
    sql = """
        SELECT users.*, COUNT(tasks.id) AS task_count
        FROM users
        LEFT JOIN tasks ON tasks.user_id = users.id
        GROUP BY users.id;
    """

    return execute_query(sql, ())


def get_users_by_parameter(column: str, value: str, exact_match: bool = True) -> list[tuple]:
    """
    Finds users based on a specified column and value, with an option for exact or pattern matching.
    :param column: The column name to search by (e.g., 'email', 'name').
    :param value: The value to search for (exact or pattern).
    :param exact_match: If True, performs exact match; if False, uses pattern matching (LIKE).
    :return: A list of users matching the search criteria.
    """
    if exact_match:
        sql = f"SELECT * FROM users WHERE {column} = ?;"
    else:
        sql = f"SELECT * FROM users WHERE {column} LIKE ?;"
        value = f"%{value}%"

    return execute_query(sql, (value,))


def update_user(data: dict, user_id: int) -> int:
    """
    Updates a user record in the database with the provided data.
    :param data: A dictionary containing column-value pairs to update.
                 For example: {"email": "newemail@example.com", "name": "New Name"}
    :param user_id: The ID of the user to be updated (integer).
    :return: An integer representing the number of rows affected by the query.
             Returns 1 if the user was updated successfully, 0 if no rows were affected.
    """
    if not data:
        raise ValueError("Data for update cannot be empty.")

    set_clause = ", ".join(f"{key} = ?" for key in data.keys())
    sql = f"""
        UPDATE users
        SET {set_clause}
        WHERE id = ?;
    """

    params = tuple(data.values()) + (user_id,)

    return execute_write(sql, params)


def print_users(users: list) -> None:
    """
    Prints the list of users.
    :param users: A list of users to display.
    :return: None
    """
    if not users:
        print("No users available.")
        print('\n')
        return

    print("Users:")
    for user in users:
        print(user)

    print('\n')


def print_user_result(rows: int, action: str) -> None:
    """
    Prints a message about the result of a user-related operation.
    :param rows: The number of rows affected by the operation.
    :param action: The type of action performed (e.g., 'updated', 'added', 'deleted').
    :return: None
    """
    action = action.lower()
    if action not in {"updated", "added", "deleted"}:
        raise ValueError("Action must be one of: 'updated', 'added', 'deleted'.")

    print(f"{rows} user(s) have been {action}." if rows > 0 else f"No user(s) were {action}.")
    print('\n')
