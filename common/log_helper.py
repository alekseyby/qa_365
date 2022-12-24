import os
import logging

"""
As need to write logs for whole module in one file, set name as (__name__)
If need to create separate file, set any unique name, eg.(TEST_CASE_1)
Usage Example:
log = log_helper.get_logger(__name__)
log.info(f'Message to log')

Log levels, from high to low:

CRITICAL
ERROR
WARNING
INFO
DEBUG
"""


LOG_FORMAT = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
LOG_LEVEL = os.environ.get('FILE_LOG_LEVEL')


def get_file_handler(name):
    file_handler = logging.FileHandler(f'{name}.log', delay=True)  # delay=True to avoid empty log files creating
    file_handler.setLevel(os.environ.get('FILE_LOG_LEVEL'))
    file_handler.setFormatter(logging.Formatter(LOG_FORMAT))
    return file_handler


def get_stream_handler():
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(logging.Formatter(LOG_FORMAT))
    return stream_handler


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(get_file_handler(name))
    logger.addHandler(get_stream_handler())
    return logger
