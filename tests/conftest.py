import allure
import pytest
from playwright.sync_api import Browser, Page
from allure_commons.types import AttachmentType


from config.config import Config


@pytest.fixture(scope="class")
def setup(request, browser: Browser, browser_context_args: dict):
    context = browser.new_context(**browser_context_args)
    page = context.new_page()
    request.cls.page = page
    # page.goto(Config.BASE_URL)
    yield page
    context.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot_path = f"reports/{item.name}_failure.png"
            page.screenshot(path=screenshot_path)
