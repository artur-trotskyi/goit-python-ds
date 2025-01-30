from seeds import populate_database
from db_functions import *
from db import db


def main():
    try:
        if db.cats.count_documents({}) == 0:
            populate_database(50)
            print("Database populated successfully!")

        print("\nРеалізуйте функцію для виведення всіх записів із колекції.")
        cats = get_all_items()
        print(cats)

        print(
            "\nРеалізуйте функцію, яка дозволяє користувачеві ввести ім'я кота та виводить інформацію про цього кота.")
        cat = get_by_attribute_value('name', 'Барсик')
        print(cat)

        print("\nСтворіть функцію, яка дозволяє користувачеві оновити вік кота за ім'ям.")
        result = update_by_name(name='Барсик', attribute='name', new_value='Кабасік')
        print(result)

        print("\nСтворіть функцію, яка дозволяє додати нову характеристику до списку features кота за ім'ям.")
        cat = add_feature_item_by_name('Кабасік', 'new feature')
        print(cat)

        print("\nРеалізуйте функцію для видалення запису з колекції за ім'ям тварини.")
        result = delete_by_attribute_value(attribute='name', value='Кабасік')
        print(result)

        print("\nРеалізуйте функцію для видалення всіх записів із колекції.")
        result = delete_all_items()
        print(result)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()
