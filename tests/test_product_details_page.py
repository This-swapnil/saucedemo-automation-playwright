from itertools import product

import allure
import pytest
from allure_commons.types import AttachmentType
from PageObjects.product_details_page import ProductDetailsPage
from PageObjects.product_list_page import ProductListPage
from utilities.base_class import BaseClass


class TestProductDetailPage(BaseClass):

    @pytest.mark.order(1)
    def test_user_login(self, get_logger):
        log = get_logger
        log.info("Step 1: Perform complete login")
        self.perform_complete_login()
        log.info("Login Successful")

    @pytest.mark.order(2)
    def test_product_name_and_price(self, get_logger) -> None:
        log = get_logger
        log.info(
            "==== Verify the names and prices of the products are in sync on PLP and PDP ===="
        )

        pdp = ProductDetailsPage(self.page)

        log.info("Step2: select a random product from PLP")
        product_name_on_plp, product_price_on_plp, _ = pdp.select_random_product()

        log.info(
            f"Name of the selected product on PLP page: {product_name_on_plp} and price: {product_price_on_plp}"
        )

        product_name_on_pdp = pdp.get_product_name()
        product_price_on_pdp = pdp.get_product_price()

        log.info(
            f"Name of the selected product on PDP page: {product_name_on_pdp} and price: {product_price_on_pdp}"
        )
        log.info(
            "Step3: Verify the names and prices of the selected products are in sync acress the PDP and PLP pages"
        )
        try:
            assert product_name_on_pdp == product_name_on_plp
            assert product_price_on_pdp == product_price_on_plp
            log.info(
                "-> Test product name and price is successful: product name and price on PLP and PDP are in sync <-"
            )
            log.info("**** Test Product Name and Price Completed ****")
        except AssertionError as e:
            log.error(f"Eror: {e}")
            allure.attach(
                self.page.screenshot(), "evidence", attachment_type=AttachmentType.PNG
            )
            log.error(
                "-> Test product name and price is unsuccessful; product name and price on PLP and PDP are not in sync <-"
            )
            raise

    @pytest.mark.order(3)
    def test_back_to_plp(self, get_logger) -> None:
        log = get_logger
        log.info(
            "==== Verify the names and prices of the products are in sync on PLP and PDP ===="
        )
        # log.info("Step 1: Perform complete login")
        # self.perform_complete_login()
        # log.info("Login Successful")
        pdp = ProductDetailsPage(self.page)
        log.info("Step2: Select a random product on PDP")
        if pdp.back_to_plp_btn.is_visible():
            log.info("Navigate back to PLP")
            pdp.click_back_to_products()
        pdp.select_random_product()  # ===============================
        log.info("Verify product is selected and redirected to PDP")
        log.info("Step3: Click back to products button")
        pdp.click_back_to_products()

        try:
            assert pdp.is_product_heding_exist()
            log.info("Products listing page is displayed with the 'Products' heading")
            log.info("**** Test Back to Product List Page Successful ****")
        except AssertionError as e:
            log.error(f"Product heading verification failed: {e}")
            allure.attach(
                self.page.screenshot(),
                "evidence",
                attachment_type=AttachmentType.PNG,
            )
            log.error("**** Test Back to Product List Page Unsuccessful ****")
            raise

    @pytest.mark.order(4)
    def test_add_to_cart(self, get_logger):
        log = get_logger
        log.info(
            "==== Verify add to cart functionality is working as expected from PDP ===="
        )
        # log.info("Step 1: Perform complete login")
        # self.perform_complete_login()
        # log.info("Login Successful")
        cart_items = 0
        pdp = ProductDetailsPage(self.page)
        plp = ProductListPage(self.page)

        plp.empty_cart()

        log.info(
            "Step2: Select a random product and navidate to its PDP and click on add to cart"
        )
        if (
            pdp.back_to_plp_btn.is_visible()
        ):  # ++++++++++++++++++++++++++++++++++++++++++++
            log.info("Navigate back to PLP")
            pdp.click_back_to_products()
        first_product_name, _, _ = pdp.select_random_product()
        pdp.click_add_to_cart()
        self.page.wait_for_timeout(10000)

        log.info("Item added to the cart")
        cart_items += 1
        log.info("Step3: Get the actual number of cart items")
        actual_cart_items = plp.get_number_of_cart_item()
        try:
            assert actual_cart_items == cart_items
            log.info("add to cart on PDP is working as expected")
            log.info("Navigate back to the PLP page and select a different product")
            pdp.click_back_to_products()
            second_product_name, _, _ = pdp.select_random_product()
            if first_product_name != second_product_name:
                log.info("Second product is selected")
                log.info("Click on Add to Cart on its PDP")
                pdp.click_add_to_cart()
                cart_items += 1
                log.info("Verify cart items are increased by 1")
                actual_cart_items = plp.get_number_of_cart_item()
                assert actual_cart_items == cart_items
                pdp.click_remove_button()
                cart_items -= 1
                actual_cart_items = plp.get_number_of_cart_item()
                assert actual_cart_items == cart_items
                log.info("**** Test Add to Cart Successful ****")
        except AssertionError as e:
            log.error(f"Error on Test Add to Cart: {e}")
            allure.attach(
                self.page.screenshot(),
                "evidence",
                attachment_type=AttachmentType.PNG,
            )
            raise

    # @pytest.mark.skip
    @pytest.mark.order(5)
    def test_remove_button(self, get_logger):
        log = get_logger
        log.info(
            "==== Verify remove button functionality is working as expected from PDP ===="
        )
        # log.info("Step 1: Perform complete login")
        # self.perform_complete_login()
        # log.info("Login Successful")

        cart_items = 0
        pdp = ProductDetailsPage(self.page)
        plp = ProductListPage(self.page)

        log.info(f"URL before empty_cart: {self.page.url}")

        if pdp.back_to_plp_btn.is_visible():
            log.info("Navigate back to PLP")
            pdp.click_back_to_products()

        plp.empty_cart()

        actual_cart_items = plp.get_number_of_cart_item()
        log.info(f"Cart items after empty_cart: {actual_cart_items}")

        assert plp.get_number_of_cart_item() == 0, "Cart is not empty"

        log.info(f"URL after empty_cart: {self.page.url}")

        log.info("Step2: Add any random product to cart")
        pdp.add_random_product_to_cart()
        cart_items += 1
        log.info("Step3: Click on remove button on PDP")
        pdp.click_remove_button()
        cart_items -= 1
        actual_cart_items = plp.get_number_of_cart_item()
        try:
            assert actual_cart_items == cart_items
            log.info("Remove button is working as expected")
            log.info("**** Test Remove Button Successful ****")
        except AssertionError as e:
            log.error(f"Remove button is not working as expected: {e}")
            allure.attach(
                self.page.screenshot(),
                "evidence",
                attachment_type=AttachmentType.PNG,
            )
            raise
