from task_manager.data.create_db import create_db
from task_manager.data.seed import generate_fake_data, insert_data_to_db
from task_manager.services.tasks import get_user_tasks, print_tasks, get_tasks_by_status, update_task_status, \
    generate_fake_task, add_task, delete_task, print_task_result, get_task_count_by_status, get_tasks_by_user_email, \
    get_tasks_without_description
from task_manager.services.users import print_users, get_users_by_parameter, update_user, \
    print_user_result, get_users_with_no_tasks, get_users_with_tasks_by_status, get_users_and_task_count


def main():
    create_db()
    users, statuses, tasks = generate_fake_data(number_users=5, number_tasks=100)
    insert_data_to_db(users, statuses, tasks)

    print('Отримати всі завдання певного користувача')
    user_id = 2
    tasks = get_user_tasks(user_id)
    print_tasks(tasks)

    print('Вибрати завдання за певним статусом')
    tasks = get_tasks_by_status('new')
    print_tasks(tasks)

    print('Оновити статус конкретного завдання')
    task_rows = update_task_status('completed', 1)
    print_task_result(task_rows, 'updated')

    print('Отримати список користувачів, які не мають жодного завдання')
    users = get_users_with_no_tasks()
    print_users(users)

    print('Додати нове завдання для конкретного користувача')
    task_data = generate_fake_task(user_id)
    task_rows = add_task(task_data)
    print_task_result(task_rows, 'added')

    print('Отримати всі завдання, які ще не завершено')
    tasks = get_tasks_by_status('completed', except_status=True)
    print_tasks(tasks)

    print('Видалити конкретне завдання')
    task_id = 1
    task_rows = delete_task(task_id)
    print_task_result(task_rows, 'deleted')

    print('Знайти користувачів з певною електронною поштою')
    users = get_users_by_parameter('email', 'example@gmail.com')
    print_users(users)
    print('Знайти користувачів з певною електронною поштою')
    users = get_users_by_parameter('email', '.com', exact_match=False)
    print_users(users)

    print("Оновити ім'я користувача")
    update_data = {"fullname": "John Doe"}
    user_rows = update_user(update_data, user_id=user_id)
    print_user_result(user_rows, 'updated')

    print('Отримати кількість завдань для кожного статусу')
    tasks = get_task_count_by_status()
    print_tasks(tasks)

    print('Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти')
    tasks = get_tasks_by_user_email('.net')
    print_tasks(tasks)

    print('Отримати список завдань, що не мають опису')
    tasks = get_tasks_without_description()
    print_tasks(tasks)

    print("Вибрати користувачів та їхні завдання, які є у статусі 'in progress'")
    users = get_users_with_tasks_by_status('in progress')
    print_users(users)

    print('Отримати користувачів та кількість їхніх завдань')
    users = get_users_and_task_count()
    print_users(users)


if __name__ == '__main__':
    print('Hello Python Docker world!\n')

    main()
