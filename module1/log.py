from my_logger import logger


def baz(num: int):
    logger.info(f"Start function baz")
    foo_ = 100
    result = foo_ + num
    logger.debug(f"result: {result}")
    return result


def foo():
    logger.error("AAAAAA!!!!")


if __name__ == '__main__':
    baz(10045)
    foo()
