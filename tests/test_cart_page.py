import random

import allure
import pytest
from allure_commons.types import AttachmentType
from PageObjects.Cart_Page import CartPage
from PageObjects.product_details_page import ProductDetailsPage
from PageObjects.product_list_page import ProductListPage
from utilities.base_class import BaseClass


class TestCartPage(BaseClass):
    @pytest.mark.order(1)
    def test_user_login(self, get_logger):
        log = get_logger
        log.info("Step 1: Perform complete login")
        self.perform_complete_login()
        log.info("Login Successful")

    @pytest.mark.order(2)
    def test_cart_heading(self, get_logger):
        """Validating if your cart heading exist"""
        log = get_logger
        log.info("Verify cart page heading is displayed as expected")
        cart_page = CartPage(self.page)
        plp = ProductListPage(self.page)
        # pdp = ProductDetailsPage(self.page)  # Use this instead of plp if continuos execution
        log.info(
            "Step2: Click on Cart button from PLP page"
        )  # Use this is seperate execution
        plp.click_cart_button()
        # pdp.click_cart_button()

        log.info("Verify on cart page the heading of Cart os displayed")
        try:
            assert cart_page.is_cart_heading_visible()
            log.info("Cart page heading is dispalyed as expected")
            log.info("**** Test Cart Heading Successful ****")
        except AssertionError as e:
            log.error(f"Cart heading is not dispalyed; Error: {e}")
            allure.attach(
                self.page.screenshot(),
                "evidence",
                attachment_type=AttachmentType.PNG,
            )
            log.error("**** Test Cart Heading Failed ****")
            raise

    @pytest.mark.order(3)
    def test_checkout_button(self, get_logger):
        """Validating the checkout button"""

        log = get_logger
        cart_page = CartPage(self.page)
        pdp = ProductDetailsPage(self.page)
        log.info("Step2: Click on Cart Icon")
        pdp.click_cart_button()
        try:
            assert cart_page.is_cart_heading_visible()
            log.info("Cart page heading is dispalyed as expected")
            cart_page.click_checkout_button()
            try:
                assert cart_page.is_checkout_page_heading_exists()
                log.info("Checkout button is working as expected")
                log.info("**** Test Checkout Button Successful ****")
            except AssertionError as e:
                log.error(f"Checkout button is not functioning properly; Error: {e}")
                allure.attach(
                    self.page.screenshot(),
                    "evidence",
                    attachment_type=AttachmentType.PNG,
                )
                log.error("**** Test Checkout Button Failed ****")
        except AssertionError as e:
            log.error(f"Cart heading is not dispalyed; Error: {e}")
            allure.attach(
                self.page.screenshot(),
                "evidence",
                attachment_type=AttachmentType.PNG,
            )
            log.error("**** Test Checkout Button Failed ****")
            raise

    @pytest.mark.order(4)
    def test_continue_shopping(self, get_logger):
        """Validating the Contine Shopping Button"""
        log = get_logger
        cart_page = CartPage(self.page)
        pdp = ProductDetailsPage(self.page)
        pdp = ProductDetailsPage(self.page)
        log.info("Step2: Click on Cart Icon")
        pdp.click_cart_button()
        log.info('Step3: Click on "Continue Shopping" button')
        cart_page.click_continue_shopping()
        pdp = ProductDetailsPage(self.page)
        plp = ProductListPage(self.page)
        log.info("Step4: Verify user is redirected to Product Listing Page (PLP)")
        curr_page_title = self.page.locator(".title").inner_text()
        plp_page_title = plp.get_page_heading()
        log.info(
            f"Current page Title: {curr_page_title} and PLP page title: {plp_page_title}"
        )
        try:
            assert curr_page_title == plp_page_title
            log.info("User is on PLP and heading of 'Products' is displayed")
            log.info("**** Test Continue Shopping Button Successful ****")
        except AssertionError as e:
            log.error(f"User is not redirected to PLP; Error: {e}")
            allure.attach(
                self.page.screenshot(),
                "evidence",
                attachment_type=AttachmentType.PNG,
            )
            log.error("User is not navigate to PLP after clicking on Continue shopping")
            log.error("**** Test Continue Shopping Button Failed ****")
            raise

    @pytest.mark.order(5)
    def test_remove_from_cart(self, get_logger):
        """Validating the Contine Shopping Button"""
        log = get_logger
        log.info("Verify remove button is working as expected")
        cart_page = CartPage(self.page)
        plp = ProductListPage(self.page)
        pdp = ProductDetailsPage(self.page)

        log.info("Step2: Select all product and add to cart")
        plp.add_all_products_to_cart()
        log.info("Step3: cilck on cart button")
        plp.click_cart_button()
        cart_items = cart_page.get_cart_items()
        log.info(
            "Verify if cart items are present and then validate the remove button's funsionality"
        )

        if cart_items:
            log.info("Select a random product from the cart")
            random_product = random.choice(cart_items)
            self.page.screenshot(path="reports/cart.png", full_page=True)
            log.info("Remove that product using remove button")
            cart_page.remove_cart_item(random_product)
            log.info("Get the current items in number")
            current_cart_items = cart_page.get_cart_items()
            # Checking if cart item is removed from cart and list is updated
            try:
                assert len(current_cart_items) < len(cart_items)
                log.info(
                    "Current cart item are less than actual once so remove button is working fine."
                )
                # Checking the cart item numbers are updated
                try:
                    assert plp.get_number_of_cart_item() == len(current_cart_items)
                    log.info("Cart items on PLP and actual cart have same data")
                    log.info("**** Test Remove From Cart Successful ****")
                except AssertionError as e:
                    log.error("Error or mismatch in cart items on PLP and cart")
                    log.error(f"Item not removed; Error: {e}")
                    allure.attach(
                        self.page.screenshot(),
                        "evidence",
                        attachment_type=AttachmentType.PNG,
                    )
                    log.error("**** Test Remove From Cart Failed ****")
            except AssertionError as e:
                log.error("Error or mismatch in cart items on PLP and cart")
                log.error(f"Item not removed; Error: {e}")
                allure.attach(
                    self.page.screenshot(),
                    "evidence",
                    attachment_type=AttachmentType.PNG,
                )
                log.error("**** Test Remove From Cart Failed ****")
                raise

    @pytest.mark.order(6)
    def test_empty_cart_checkout(self, get_logger):
        """Verifying user is not able to proceed if cart is empty"""
        log = get_logger
        log.info("==== Verify user is not able to proceed if cart is empty. ====")
        cart_page = CartPage(self.page)
        plp = ProductListPage(self.page)

        log.info("Step1: Empty cart is it has items")
        plp.empty_cart()
        plp.click_cart_button()
        log.info("Verify on cart page, the heding of cart is displayed")
        try:
            assert len(cart_page.get_cart_items()) == 0
            cart_page.click_checkout_button()
            log.info("Verify user is unable to proceed with checkout")
            try:
                assert cart_page.is_cart_heading()
                log.info("User is unable to proceed with the cart having 0 items in it")
                log.info("**** Test Empty Cart Checkout Successful ****")
            except AssertionError as e:
                log.error("User is able to proceed having 0 items")
                allure.attach(
                    self.page.screenshot(),
                    "evidence",
                    attachment_type=AttachmentType.PNG,
                )
                log.error("**** Test Empty Cart Checkout Failed ****")
        except AssertionError as e:
            log.error("User is able to proceed having 0 items")
            allure.attach(
                self.page.screenshot(),
                "evidence",
                attachment_type=AttachmentType.PNG,
            )
            log.error("**** Test Empty Cart Checkout Failed ****")
            raise
