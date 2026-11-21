import re

from playwright.sync_api import Page, expect, Locator
from config.config import Config


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.page.set_default_timeout(Config.DEFAULT_TIMEOUT)

    def navigate(self, url: str = Config.BASE_URL) -> None:
        self.page.goto(url=url)

    def get_locator(self, selector: str) -> Locator:
        return self.page.locator(selector)

    def click(self, selector: str) -> None:
        self.get_locator(selector=selector).click()

    def fill(self, selector: str, text: str) -> None:
        self.get_locator(selector=selector).fill(text)

    def get_text(self, selector: str) -> str:
        return self.get_locator(selector=selector).inner_text()

    def get_url(self) -> str:
        return self.page.url

    def is_visible(self, selector: str) -> bool:
        return self.get_locator(selector=selector).is_visible()

    def assert_url_contains(self, substring: str) -> None:
        expect(self.page).to_have_url(re.compile(f".*{re.escape(substring)}.*"))

    def assert_text_visible(self, selector: str, expected_Text: str) -> None:
        expect(self.get_locator(selector=selector)).to_have_text(expected=expected_Text)
