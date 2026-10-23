# pip install loguru
import sys

from loguru import logger


@logger.catch
def do_something( a, b ):
    logger.debug(f"Аргументи: {a, b}")
    try:
        a / b
    except ZeroDivisionError:
        return logger.error("Неможна ділити на нуль")
    return a / b
