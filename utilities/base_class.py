import inspect
import logging

import pytest
from playwright.sync_api import Page

from PageObjects.login_page import LoginPage


@pytest.mark.usefixtures("setup")
class BaseClass:
    page: Page

    @pytest.fixture(scope="module", autouse=True)
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

    def perform_complete_login(self):
        login_page = LoginPage(self.page)
        login_page.login(username="standard_user", password="secret_sauce")
