from math import prod
import random

from PageObjects.base_page import BasePage
from PageObjects.product_list_page import ProductListPage
from playwright.sync_api import Locator, expect


class ProductDetailsPage(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)

        # Locators
        self.product_name_locator = page.locator(".inventory_details_name")
        self.product_price_locator = page.locator(".inventory_details_price")
        self.add_to_cart_btn = page.locator("#add-to-cart")
        self.remove_btn = page.get_by_role("button", name="Remove", exact=True)
        self.back_to_plp_btn = page.locator("#back-to-products")
        self.heading_locator = page.locator(".title")
        self.cart_locator = page.locator(".shopping_cart_link")
        self.cart_items = page.locator(".cart_item")

    # Get methods
    def get_product_name(self) -> str:
        return self.get_text(self.product_name_locator)

    def get_product_price(self) -> str:
        return self.get_text(self.product_price_locator)

    def get_cart_items_count(self) -> int:
        return self.cart_items.count()

    # click methods
    def click_back_to_products(self) -> None:
        self.click(self.back_to_plp_btn)

    def click_add_to_cart(self) -> None:
        self.click(self.add_to_cart_btn)

    def click_remove_button(self) -> None:
        self.click(self.remove_btn)

    def click_cart_button(self) -> None:
        self.click(self.cart_locator)

    # Complete action method
    def select_random_product(self) -> tuple[str, str, Locator]:
        plp_page = ProductListPage(self.page)
        all_products = plp_page.get_all_products()

        # Wait until products are loaded
        expect(all_products.first).to_be_visible(timeout=10000)

        product_count = all_products.count()

        if product_count == 0:
            raise RuntimeError("No products available on the prouct listing page")

        # select a random product
        random_idx = random.randrange(product_count)
        product = all_products.nth(random_idx)

        # Get product details before navigating
        product_name = product.locator(".inventory_item_name").inner_text()
        product_price = product.locator(".inventory_item_price").inner_text()

        # Click the selected product
        product.locator(".inventory_item_name").click()

        # Verify succesful navigation to PDP
        expect(self.product_name_locator).to_have_text(product_name)

        return product_name, product_price, product

    def add_random_product_to_cart(self) -> None:
        self.select_random_product()
        self.click_add_to_cart()

        expect(self.remove_btn).to_be_visible()

    def is_product_heding_exist(self) -> bool:
        return self.heading_locator.is_visible()
