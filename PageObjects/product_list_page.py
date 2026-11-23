from ast import List

from playwright.sync_api import Page, Locator

from PageObjects.base_page import BasePage


class ProductListPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        # Locators
        self.cart_buttons = page.locator("button:has-text('Add to cart')")  # List
        self.remove_buttons = page.locator("button:has-text('Remove')")  # List
        self.cart_badge = page.locator(".shopping_cart_badge")  # cart item total count
        self.cart_icon_button = page.locator(".shopping_cart_link")  # cart icon

        self.products = page.locator(".inventory_item")  # $29.99
        self.product_names = page.locator(
            ".inventory_item_name"  # Sauce Labs Backpack, Sauce Labs Bike Light
        )
        self.product_prices = page.locator(".inventory_item_price")

        self.hamburger_menu = page.locator("#react-burger-menu-btn")
        self.page_heading = page.locator(".title")
        self.filter_dropdown = page.locator(".product_sort_container")

    # Get Methods
    def get_all_products(self) -> Locator:
        return self.products

    def get_all_product_names(self) -> list[str]:
        return self.product_names.all_inner_texts()

    def get_all_product_prices(self) -> list[str]:
        return self.product_prices.all_inner_texts()

    def get_page_heading(self) -> str:
        return self.get_text(self.page_heading)

    def get_number_of_cart_item(self) -> int:
        return (
            int(self.get_text(self.cart_badge))
            if self.is_visible(self.cart_badge)
            else 0
        )

    def get_list_of_products_by_price(self, price: str) -> Locator:
        price = price.replace("$", "")
        return self.products.filter(has=self.page.get_by_text(price, exact=True))

    def get_list_of_products_by_title(self, title: str) -> Locator:
        return self.products.filter(
            has=self.product_names.get_by_text(title, exact=True)
        )

    # Click methods
    def click_hamburger_menu(self) -> None:
        self.click(self.hamburger_menu)

    def click_cart_button(self) -> None:
        self.click(self.cart_icon_button)

    # Sort mehhod
    def sort(self, sort: str) -> None:
        match sort:
            case "A_to_Z":
                self.filter_dropdown.select_option(label="Name (A to Z)")
            case "Z_to_A":
                self.filter_dropdown.select_option(label="Name (Z to A)")
            case "low_high":
                self.filter_dropdown.select_option(label="Price (low to high)")
            case "high_low":
                self.filter_dropdown.select_option(label="Price (high to low)")
            case _:
                raise ValueError(f"Invalid sort option: {sort}")

    # Cart Methods
    def add_all_products_to_cart(self) -> None:
        if self.remove_buttons.count() > 0:
            self.empty_cart()
        while self.cart_buttons.count() > 0:
            self.cart_buttons.first.click()

    def add_to_cart_products_by_title(self, title: str) -> None:
        product = self.get_list_of_products_by_title(title=title)
        product.get_by_role("button", name="Add to cart").click()

    def add_to_cart_product_by_price(self, price: str) -> None:
        products = self.get_list_of_products_by_price(price=price)
        for index in range(products.count()):
            products.nth(index=index).get_by_role("button", name="Add to cart").click()

    def empty_cart(self) -> None:
        while self.remove_buttons.count() > 0:
            self.remove_buttons.first.click()
