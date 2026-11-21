import inspect
import logging

import pytest


class BaseClass:
    @pytest.fixture(scope="module")
    def get_logger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)

        fh = logging.FileHandler("logs/logging.log")
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(
            logging.Formatter(
                "%(asctime)s - [%(module)s] - [%(filename)s:%(lineno)d] - "
                "[%(funcName)s - [%(levelname)s] - %(message)s"
            )
        )
        logger.addHandler(fh)
        return logger
