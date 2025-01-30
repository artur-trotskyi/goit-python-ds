from typing import Any
from pymongo.results import DeleteResult
from db import db
from decorators import handle_db_errors


@handle_db_errors
def get_all_items() -> list:
    """
    Fetch all records from the 'cats' collection.
    Returns:
        list: A list of all documents in the 'cats' collection.
    """
    return list(db.cats.find())


@handle_db_errors
def get_by_attribute_value(attribute: str, value: str) -> dict | None:
    """
    Fetch a single record from the 'cats' collection based on a given attribute and value.
    Args:
        attribute (str): The name of the attribute to search by.
        value (str): The value of the attribute to match.
    Returns:
        dict | None: The first document that matches the given attribute and value, or None if no match is found.
    """
    return db.cats.find_one({attribute: value})


@handle_db_errors
def update_by_name(name: str, attribute: str, new_value: Any) -> int:
    """
    Updates the value of a specific attribute for record with the given name.
    Args:
        name (str): The name of the cat to update.
        attribute (str): The attribute to be updated.
        new_value (Any): The new value for the attribute.
    Returns:
        int: The number of documents that were updated.
    """
    result = db.cats.update_one(
        {"name": name},
        {"$set": {attribute: new_value}}
    )

    return result.modified_count


@handle_db_errors
def add_feature_item_by_name(name_value: str, feature_item: Any) -> dict:
    """
    Adds a new feature to the 'features' list of a cat by its name.
    Args:
        name_value (str): The name of the cat to which the feature should be added.
        feature_item (Any): The feature to be added to the cat's 'features' list.
    Returns:
        dict: The updated cat document if found, or an empty dictionary if the cat is not found.
    """
    cat = get_by_attribute_value('name', name_value)
    if cat is None:
        return {}

    cat.get('features').append(feature_item)
    db.cats.update_one(
        {"name": name_value},  # Condition to search for the cat by its name
        {"$set": {"features": cat['features']}}  # Updating the 'features' list
    )

    return cat


@handle_db_errors
def delete_by_attribute_value(attribute: str, value: Any) -> DeleteResult:
    """
    Deletes a document from the 'cats' collection based on a specific attribute value.
    Args:
        attribute (str): The name of the attribute to search by.
        value (Any): The value of the attribute to match for deletion.
    Returns:
        DeleteResult: The result of the delete operation.
    """

    return db.cats.delete_one({attribute: value})


@handle_db_errors
def delete_all_items() -> DeleteResult:
    """
    Deletes all records from the 'cats' collection in the database.
    Returns:
        DeleteResult: The result of the delete operation, which includes
                      information about the number of deleted documents.
    """

    return db.cats.delete_many({})
