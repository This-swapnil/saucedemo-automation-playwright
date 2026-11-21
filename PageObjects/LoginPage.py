from playwright.sync_api import Page, Locator

from PageObjects.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        # self.navigate()

    # Locators
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MSG = ".error-message-container"
    TITLE = ".title"

    def login(self, username: str, password: str) -> None:
        self.fill(selector=self.USERNAME_INPUT, text=username)
        self.fill(selector=self.PASSWORD_INPUT, text=password)
        self.click(self.LOGIN_BUTTON)

    def error_msg(self) -> str:
        error_msg = self.get_text(selector=self.ERROR_MSG).split(":")[1]
        return error_msg

    def error_message_exists(self):
        return True if self.is_visible(selector=self.ERROR_MSG) else False

    def title_exists(self):
        return True if "Products" in self.get_text(selector=self.TITLE) else False
