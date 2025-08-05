import logging

from loguru import logger


def hack_logger():
    """hack第三方库的logger到luguru"""

    class InterceptHandler(logging.Handler):
        def emit(self, record: logging.LogRecord) -> None:
            try:
                level = logger.level(record.levelname).name
            except ValueError:
                level = record.levelno
            frame, depth = logging.currentframe(), 2
            while frame and (frame.f_code.co_filename == logging.__file__):
                frame = frame.f_back
                depth += 1
            logger.opt(depth=depth, exception=record.exc_info).log(
                level, record.getMessage()
            )

    logging.basicConfig(handlers=[InterceptHandler()], level=logging.INFO)

    for name in logging.root.manager.loggerDict:
        existing_logger = logging.getLogger(name)
        existing_logger.handlers = []
        existing_logger.addHandler(InterceptHandler())


def setup_logger():
    hack_logger()
