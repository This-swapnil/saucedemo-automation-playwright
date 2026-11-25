from PageObjects.base_page import BasePage
from playwright.sync_api import Locator


class CartPage(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)

        self.heading_locator = page.locator(".title")  # "Your Cart"
        self.checkout_btn = page.locator("#checkout")
        self.continue_shopping_btn = page.locator("#continue-shopping")
        self.checkout_page_heading = page.locator(
            ".title"
        )  # "Checkout: Your Information" next page
        self.cart_items = page.locator(".cart_item")
        self.remove_btn = page.locator("#remove-sauce-labs-backpack")

    def is_cart_heading_visible(self) -> bool:
        return self.is_visible(self.heading_locator)

    def is_cart_heading(self) -> bool:
        heading = self.get_text(self.heading_locator)
        return True if "Cart" in heading else False

    def click_checkout_button(self) -> None:
        self.click(self.checkout_btn)

    def click_continue_shopping(self) -> None:
        self.click(self.continue_shopping_btn)

    def is_checkout_page_heading_exists(self) -> bool:
        return self.is_visible(self.checkout_page_heading)

    def get_cart_items(self) -> list[Locator]:
        return self.cart_items.all()

    def remove_cart_item(self, item: Locator) -> None:
        remove_btn = item.locator("button:has-text('Remove')")
        remove_btn.click()
