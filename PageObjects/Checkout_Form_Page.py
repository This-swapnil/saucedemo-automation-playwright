from PageObjects.Checkout_Page import CheckoutPage
from PageObjects.base_page import BasePage


class CheckoutFormPage(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)

        # Locators
        self.title_text = page.locator(".title")
        self.first_name = page.locator("#first-name")
        self.last_name = page.locator("#last-name")
        self.post_code = page.locator("#postal-code")
        self.cancel_btn = page.locator("#cancel")
        self.continue_btn = page.locator("#continue")
        self.error_msg = page.locator(".error-message-container")
        self.chkout_overview_page_title = page.locator(".title")

    # Get methods
    def get_information_page_heading(self) -> str:
        return self.get_text(self.title_text)

    def get_chckout_overview_page_heading(self) -> str:
        return self.get_text(self.chkout_overview_page_title)

    def get_first_name(self) -> str:
        return self.title_text.get_attribute("value")

    def get_last_name(self) -> str:
        return self.last_name.get_attribute("value")

    def get_post_code(self) -> str:
        return self.post_code.get_attribute("value")

    def get_error_msg(self) -> str:
        return self.get_text(self.error_msg)

    def get_confinue_btn(self):
        self.click(self.continue_btn)
        checkout_page = CheckoutPage(self.page)
        return checkout_page

    # Click methods
    def click_cancel_btn(self) -> None:
        self.click(self.cancel_btn)

    def click_continue_btn(self) -> None:
        self.click(self.continue_btn)

    # Enter data
    def enter_first_name(self, first_name) -> None:
        self.fill(self.first_name, first_name)

    def enter_last_name(self, last_name) -> None:
        self.fill(self.last_name, last_name)

    def enter_post_code(self, post_code) -> None:
        self.fill(self.post_code, post_code)

    def error_exists(self) -> bool:
        return True if self.get_error_msg() else False

    def information_page_heading_exits(self) -> bool:
        heading_text = self.get_text(self.title_text)
        return True if "Information" in heading_text else False

    # Complete action methods
    def navigate_to_checkout_overview_page(self, plp, cart_page, checkout_form_page):
        plp.click_cart_button()
        cart_page.click_checkout_button()
        checkout_form_page.click_on_continue_button()
        checkout_form_page.enter_first_name("John")
        checkout_form_page.enter_last_name("wick")
        checkout_form_page.enter_post_code("2154")
        checkout_form_page.click_on_continue_button()
        checkout_page = CheckoutPage(self.page)
        return checkout_page
