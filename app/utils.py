import sys

from loguru import logger


def setup_logging() -> None:
    logger.remove(0)
    logger.add(
        "logs/log_{time}.log",
        level="DEBUG",
        rotation="1 week",
        retention=3,
        backtrace=True,
        diagnose=True,
    )
    logger.add(
        sys.stderr, format="{message}", level="DEBUG", colorize=True, backtrace=True, diagnose=True
    )
