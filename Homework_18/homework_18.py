import os
import sys
from loguru import logger
from demo_1 import do_something

def debug_filter(record):
    return record["level"].name != "DEBUG"


logger.remove()
logger.add(sys.stderr, level="INFO", filter=debug_filter)
logger.add("Homework_18/homework.log", level="DEBUG")

logger.info(do_something(10, 0))


