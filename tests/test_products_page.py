import pytest

from PageObjects.product_list_page import ProductListPage
from tests.conftest import setup
from utilities.base_class import BaseClass
import allure
from allure_commons.types import AttachmentType


class TestProductPage(BaseClass):
    @pytest.mark.order(1)
    def test_user_login(self, get_logger):
        log = get_logger
        log.info("Step 1: Perform complete login")
        self.perform_complete_login()
        log.info("Login Successful")

    @pytest.mark.order(2)
    def test_sort_a_to_z(self, get_logger) -> None:
        log = get_logger
        """ For validating the filter for product with A to Z filter"""
        # log.info("Step 1: Perform complete login")
        # self.perform_complete_login()
        # log.info("Login Successful")
        products_page = ProductListPage(self.page)
        products_before_sort = []
        products_after_sort = []
        for product in products_page.get_all_product_names():
            products_before_sort.append(product)
        log.info("Step 2: Sort the product with A to Z order")
        products_page.sort("A_to_Z")
        for product in products_page.get_all_product_names():
            products_after_sort.append(product)
        try:
            assert products_after_sort == products_before_sort
            log.info("Products are sorted successfully (A to Z)")
        except AssertionError:
            log.error("Product are not sorted")
            allure.attach(
                self.page.screenshot(), "evidence", attachment_type=AttachmentType.PNG
            )
            pytest.fail("Products are not sorted in A to Z order.")
        log.info("**** Test sorting the products using A to Z filter Completed ****")

    @pytest.mark.order(3)
    def test_sort_z_to_a(self, get_logger) -> None:
        log = get_logger
        """For validating the filter for products with Z to A filter"""
        # log.info("Step 1: Perform complete login")
        # self.perform_complete_login(setup_page)
        # log.info("Login Successful")
        products_page = ProductListPage(self.page)
        products_before_sort = []
        products_after_sort = []
        for product in products_page.get_all_product_names():
            products_before_sort.append(product)
        log.info(f"Product name before sorting ====> {products_before_sort}")
        log.info("Step 2: Sort the product with Z to A order")
        products_page.sort("Z_to_A")
        for product in products_page.get_all_product_names():
            products_after_sort.append(product)
        log.info(f"Product name after sorting Z to A====> {products_after_sort}")
        try:
            assert products_after_sort == products_before_sort[::-1]
            log.info("Products are sorted sucessfully (Z to A)")
        except AssertionError:
            log.error("Products are not sorted (Z to A)")
            allure.attach(self.page.screenshot(), "evidence", AttachmentType.PNG)
            pytest.fail("Products are not sorted in Z to A order.")
        log.info("**** Test sorting the products using Z to A filter Completed ****")

    @pytest.mark.order(4)
    def test_sort_low_to_high(self, get_logger) -> None:
        log = get_logger
        """For validating the filter for products with low to high filter"""
        # log.info("Step 1: Perform complete login")
        # self.perform_complete_login(setup_page)
        # log.info("Login Successful")
        products_page = ProductListPage(self.page)
        products_prices_before_sort = []
        products_prices_after_sort = []
        for product in products_page.get_all_product_prices():
            products_prices_before_sort.append(product)
        log.info(f"Product name before sorting ====> {products_prices_before_sort}")
        log.info("Step 2: Sort the product with Low-to-High order")
        products_page.sort("low_high")
        for product in products_page.get_all_product_prices():
            products_prices_after_sort.append(product)
        log.info(f"Product name after sorting Z to A====> {products_prices_after_sort}")
        try:
            assert products_prices_after_sort == sorted(
                products_prices_before_sort,
                key=lambda price: float(price.replace("$", "")),
            )
            log.info("Products are sorted Successfully (Low-to-High)")
        except AssertionError:
            log.error("Products are not sorted Successfully (Low-to-High)")
            allure.attach(self.page.screenshot(), "evidence", AttachmentType.PNG)
            pytest.fail("Products are not sorted in Low-to-High order.")
        log.info(
            "**** Test sorting the products using Low-to-High filter Completed ****"
        )

    @pytest.mark.order(5)
    def test_sort_high_to_low(self, get_logger) -> None:
        log = get_logger
        """For validating the filter for products with high to low filter"""
        # log.info("Step 1: Perform complete login")
        # self.perform_complete_login()
        # log.info("Login Successful")
        products_page = ProductListPage(self.page)
        products_prices_before_sort = []
        products_prices_after_sort = []
        for product in products_page.get_all_product_prices():
            products_prices_before_sort.append(product)
        log.info(f"Product name before sorting ====> {products_prices_before_sort}")
        log.info("Step 2: Sort the product with high to low order")
        products_page.sort("high_low")
        for product in products_page.get_all_product_prices():
            products_prices_after_sort.append(product)
        log.info(
            f"Product name after sorting high to low ====> {products_prices_after_sort}"
        )
        try:
            assert products_prices_after_sort == sorted(
                products_prices_before_sort,
                key=lambda price: float(price.replace("$", "")),
                reverse=True,
            )
            log.info("Products are sorted Successfully (High-to-Low)")
        except AssertionError:
            log.error("Products are not sorted Successfully (Low-to-High)")
            allure.attach(self.page.screenshot(), "evidence", AttachmentType.PNG)
            pytest.fail("Products are not sorted in High-to-Low order.")
        log.info(
            "**** Test sorting the products using High-to-Low filter Completed ****"
        )

    @pytest.mark.order(6)
    def test_add_to_cart_all_products(self, get_logger) -> None:
        """Validating the add to cart button on PLP"""
        log = get_logger
        log.info("==== Verify user is able to add all the present product to cart")

        products_page = ProductListPage(self.page)
        log.info("Step:2 Add all the products to cart")
        products_page.add_all_products_to_cart()
        added_product = products_page.get_number_of_cart_item()
        log.info(f"Added products: {added_product}")
        all_products = products_page.get_all_products()
        log.info(f"All products: {all_products.count()}")
        try:
            assert added_product == all_products.count()
            log.info("-> Successfully added all the products to cart <-")
        except AssertionError:
            log.error("Unable to add all the products to cart")
            allure.attach(
                self.page.screenshot(), "evidence", attachment_type=AttachmentType.PNG
            )
            pytest.fail("Unanle to add all the products to cart")
        products_page.empty_cart()
        log.info("**** Test Add to Cart All Products Completed ****")

    @pytest.mark.order(7)
    def test_remove_buttons(self, get_logger) -> None:
        log = get_logger
        log.info("==== Verify the remove button in PLP after adding products to cart")
        products_page = ProductListPage(self.page)
        products_page.empty_cart()
        remove_buttons = products_page.remove_buttons
        log.info("Check no remove buttons should be displayed at start")
        assert remove_buttons.count() == 0
        log.info("No remove buttons are present")
        log.info("Adding all the products to cart")
        products_page.add_all_products_to_cart()
        all_products = products_page.get_all_products()
        products_in_cart = products_page.get_number_of_cart_item()
        log.info(
            f"Total Products in cart after adding all the products: {products_in_cart}"
        )
        try:
            assert all_products.count() == products_in_cart
            log.info("Added all the products to cart")
            log.info("Removing products using remove button")
            products_page.empty_cart()
            products_in_cart = products_page.get_number_of_cart_item()
            log.info(
                f"Total Products in cart after removing all products: {products_in_cart}"
            )
            assert products_page.remove_buttons.count() == 0
            log.info("-> All the remove buttons are functioning properly <-")
        except AssertionError:
            log.error("Remove buttons are no funcitoning properly")
            allure.attach(
                self.page.screenshot(), "evidence", attachment_type=AttachmentType.PNG
            )
            pytest.fail("Remove buttons are no funcitoning properly")
        log.info("**** Test Remove Button Completed ****")

    @pytest.mark.order(8)
    def test_add_cart_by_title(self, get_logger):
        """Validating the adding to cart functionality by giving a name of the product"""
        log = get_logger
        log.info("==== Verify user is able to add the product to cart by its title")
        products_page = ProductListPage(self.page)
        log.info("Step2: Provide the product title for adding to cart")
        product = products_page.get_list_of_products_by_title("Sauce Labs Backpack")
        log.info("Title provided for product: 'Sauce Labs Backpack'")
        log.info("Step3: Add product to cart with title 'Sauce Labs Backpack'")
        products_page.add_to_cart_products_by_title("Sauce Labs Backpack")
        try:
            assert product.count() == products_page.get_number_of_cart_item()
            log.info("-> Product with given title is added to cart <-")
        except AssertionError:
            log.error("Product with given title is not added to cart")
            allure.attach(
                self.page.screenshot(), "evidence", attachment_type=AttachmentType.PNG
            )
            pytest.fail("Product with given title is not added to cart")
        products_page.empty_cart()
        log.info("**** Test Add to Cart by Title Completed ****")

    @pytest.mark.order(9)
    def test_add_to_cart_by_price(self, get_logger):
        """Validating the adding to cart functionality by giving the price of the product"""
        log = get_logger
        log.info("==== Verify user is able to add the product to cart by its price")
        products_page = ProductListPage(self.page)
        log.info("Step2: Provide the product price for adding to cart")
        products = products_page.get_list_of_products_by_price("$7.99")
        log.info("Price provided for product: $7.99")
        log.info("Step3: Add product to cart with price $7.99")

        products_page.add_to_cart_product_by_price("$7.99")

        try:
            assert products.count() == products_page.get_number_of_cart_item()
            log.info("-> Products with given price is added to cart <-")
        except AssertionError:
            log.error("Product with given price is not added to cart")
            allure.attach(
                self.page.screenshot(), "evidence", attachment_type=AttachmentType.PNG
            )
            pytest.fail("Product with given price is not added to cart")
        products_page.empty_cart()
        log.info("**** Test Add to Cart by Price Completed ****")
