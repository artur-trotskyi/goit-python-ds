import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

log_format = "[%(levelname)s] %(asctime)s: %(name)s %(module)s %(funcName)s:%(lineno)d - %(message)s"

rotating_file_handler = RotatingFileHandler(
    "rotating_log.log",
    maxBytes=5 * 1024 * 1024,
    backupCount=3,
    encoding="utf-8"
)
rotating_file_handler.setLevel(logging.ERROR)
rotating_file_handler.setFormatter(logging.Formatter(log_format))

daily_file_handler = TimedRotatingFileHandler(
    "daily_log.log",
    when="midnight",
    interval=1,
    backupCount=7,
    encoding="utf-8"
)
daily_file_handler.setLevel(logging.ERROR)
daily_file_handler.setFormatter(logging.Formatter(log_format))

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(logging.Formatter(log_format))


def get_logger(name, level):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(stream_handler)
    logger.addHandler(rotating_file_handler)
    logger.addHandler(daily_file_handler)

    return logger


logger = get_logger('my_logger', logging.DEBUG)
