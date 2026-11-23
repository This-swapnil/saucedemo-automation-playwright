import inspect
import logging

import pytest

from PageObjects.login_page import LoginPage


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

    def perform_complete_login(self, page):
        login_page = LoginPage(page)
        login_page.login(username="standard_user", password="secret_sauce")
