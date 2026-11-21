import pytest
from playwright.sync_api import Page
from config.config import Config


@pytest.fixture(scope="function")
def setup_page(page: Page):
    page.goto(Config.BASE_URL)
    yield page


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot_path = f"reports/{item.name}_failure.png"
            page.screenshot(path=screenshot_path)
