from playwright.sync_api import Page, Locator

from PageObjects.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.navigate()

        # Locators
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error = page.locator(".error-message-container")
        self.title = page.locator(".title")

    def login(self, username: str, password: str) -> None:
        self.fill(self.username, text=username)
        self.fill(self.password, text=password)
        self.login_button.click()

    def error_msg(self) -> str:
        error_msg = self.get_text(locator=self.error).split(":")[1]
        return error_msg

    def error_message_exists(self):
        return True if self.is_visible(locator=self.error) else False

    def title_exists(self):
        return True if "Products" in self.get_text(locator=self.title) else False
