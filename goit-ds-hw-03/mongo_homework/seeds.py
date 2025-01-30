from faker import Faker
from db import db
from decorators import handle_db_errors
from typing import List, Dict, Optional


def generate_fake_item(
        fake_data: Faker,
        name: Optional[str] = None,
        age: Optional[int] = None,
        features: Optional[List[str]] = None
) -> Dict[str, int | List[str]]:
    """
    Generates a single fake item.
    Args:
        fake_data (Faker): An instance of the Faker class for generating fake data.
        name (Optional[str]): Optional name. If not provided, a fake name is generated.
        age (Optional[int]): Optional age. If not provided, a random age is generated.
        features (Optional[List[str]]): Optional list of features. If not provided, fake features are generated.
    Returns:
        dict: A dictionary representing a fake item.
    """
    return {
        "name": name if name is not None else fake_data.name(),
        "age": age if age is not None else fake_data.random_int(min=1, max=15),
        "features": features if features is not None else [
            " ".join(fake_data.words(nb=2)),
            " ".join(fake_data.words(nb=3)),
            " ".join(fake_data.words(nb=2))
        ]
    }


def generate_fake_items(fake_data: Faker, count: int) -> List[Dict[str, any]]:
    """
    Generates multiple fake items.
    Args:
        fake_data (Faker): An instance of the Faker class for generating fake data.
        count (int): The number of fake items to generate.
    Returns:
        list: A list of dictionaries representing fake items.
    """
    return [generate_fake_item(fake_data) for _ in range(count)]


@handle_db_errors
def populate_database(count: int) -> None:
    """
    Inserts generated items into the database.
    Args:
        count (int): The number of items to insert into the database.
    Returns:
        None
    """
    fake_data = Faker('uk_UA')
    fake_items = generate_fake_items(fake_data, count - 1)
    db.cats.insert_many(fake_items)

    item = generate_fake_item(fake_data, name="Барсик")
    db.cats.insert_one(item)

    print(f"{count} items inserted into the database.")
