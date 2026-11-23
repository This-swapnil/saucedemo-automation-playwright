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
        log.info("Now, verify user is able to sort the products")

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
        self.page.wait_for_timeout(5000)
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
        log.info("==== Test sorting the products using A to Z filter Completed ====")

    @pytest.mark.order(3)
    def test_sort_z_to_a(self, get_logger) -> None:
        log = get_logger
        """For validating the filter for products with Z to A filter"""
        # log.info("Step 1: Perform complete login")
        # self.perform_complete_login(setup_page)
        # log.info("Login Successful")
        products_page = ProductListPage(self.page)
        self.page.wait_for_timeout(10000)
        products_before_sort = []
        products_after_sort = []
        for product in products_page.get_all_product_names():
            products_before_sort.append(product)
        print(f"Product name before sortin ====> {products_before_sort}")
        log.info("Step 2: Sort the product with Z to A order")
        products_page.sort("Z_to_A")
        self.page.wait_for_timeout(5000)
        for product in products_page.get_all_product_names():
            products_after_sort.append(product)
        print(f"Product name after sortin Z to A====> {products_after_sort}")
        try:
            assert products_after_sort == products_before_sort[::-1]
            log.info("Products are sorted sucessfully (Z to A)")
        except AssertionError:
            log.error("Products are not sorted (Z to A)")
            allure.attach(self.page.screenshot(), "evidence", AttachmentType.PNG)
            pytest.fail("Products are not sorted in Z to A order.")
        log.info("==== Test sorting the products using Z to A filter Completed ====")

    @pytest.mark.order(4)
    def test_sort_low_to_high(self, get_logger) -> None:
        log = get_logger
        """For validating the filter for products with low to high filter"""
        # log.info("Step 1: Perform complete login")
        # self.perform_complete_login(setup_page)
        # log.info("Login Successful")
        products_page = ProductListPage(self.page)
        self.page.wait_for_timeout(10000)
        products_prices_before_sort = []
        products_prices_after_sort = []
        for product in products_page.get_all_product_prices():
            products_prices_before_sort.append(product)
        print(f"Product name before sorting ====> {products_prices_before_sort}")
        log.info("Step 2: Sort the product with Low-to-High order")
        products_page.sort("low_high")
        self.page.wait_for_timeout(5000)
        for product in products_page.get_all_product_prices():
            products_prices_after_sort.append(product)
        print(f"Product name after sortinh Z to A====> {products_prices_after_sort}")
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
            "==== Test sorting the products using Low-to-High filter Completed ===="
        )

    @pytest.mark.order(5)
    def test_sort_high_to_low(self, get_logger) -> None:
        log = get_logger
        """For validating the filter for products with high to low filter"""
        # log.info("Step 1: Perform complete login")
        # self.perform_complete_login()
        # log.info("Login Successful")
        products_page = ProductListPage(self.page)
        self.page.wait_for_timeout(10000)
        products_prices_before_sort = []
        products_prices_after_sort = []
        for product in products_page.get_all_product_prices():
            products_prices_before_sort.append(product)
        print(f"Product name before sorting ====> {products_prices_before_sort}")
        log.info("Step 2: Sort the product with high to low order")
        products_page.sort("high_low")
        self.page.wait_for_timeout(5000)
        for product in products_page.get_all_product_prices():
            products_prices_after_sort.append(product)
        print(
            f"Product name after sortinh high to low ====> {products_prices_after_sort}"
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
            "==== Test sorting the products using High-to-Low filter Completed ===="
        )
