import re

from playwright.sync_api import Page, expect, Locator
from config.config import Config


class BasePage:
    def __init__(self, page) -> None:
        self.page = page
        self.url = Config.BASE_URL
        self.page.set_default_timeout(Config.DEFAULT_TIMEOUT)

    def navigate(self) -> None:
        self.page.goto(self.url)

    # def get_locator(self, selector: str) -> Locator:
    #     return self.page.locator(selector)

    def click(self, locator: Locator) -> None:
        locator.click()

    def fill(self, locator: Locator, text: str) -> None:
        locator.clear()
        locator.fill(text)

    def get_text(self, locator: Locator) -> str:
        return locator.inner_text()

    def get_url(self) -> str:
        return self.page.url

    def is_visible(self, locator: Locator) -> bool:
        return locator.is_visible()

    # Generic Assertion
    def assert_url_contains(self, substring: str) -> None:
        expect(self.page).to_have_url(re.compile(f".*{re.escape(substring)}.*"))

    def assert_text_visible(self, locator: Locator, expected_Text: str) -> None:
        expect(locator).to_have_text(expected=expected_Text)
