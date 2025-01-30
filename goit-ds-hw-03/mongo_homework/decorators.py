from functools import wraps
import pymongo


def handle_db_errors(func):
    """
    Decorator to handle database connection errors and MongoDB exceptions.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except RuntimeError as e:
            print(f"Database connection error: {e}")
        except pymongo.errors.PyMongoError as e:
            print(f"MongoDB error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    return wrapper
