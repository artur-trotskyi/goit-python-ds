import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(funcName)5s - %(message)s")


def function_for_test_logging(num: int):
    foo = 100
    result = foo + num
    logging.debug(f"result: {result}")
    return result


if __name__ == '__main__':
    function_for_test_logging(10045)
