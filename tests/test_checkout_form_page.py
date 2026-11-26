import allure
import pytest

from PageObjects.Cart_Page import CartPage
from PageObjects.Checkout_Form_Page import CheckoutFormPage
from PageObjects.product_list_page import ProductListPage
from utilities.base_class import BaseClass
from allure_commons.types import AttachmentType


class TestCheckoutFormPage(BaseClass):

    @pytest.mark.order(1)
    def test_user_login(self, get_logger):
        log = get_logger
        log.info("Step 1: Perform complete login")
        self.perform_complete_login()
        log.info("Login Successful")

    @pytest.mark.order(2)
    def test_information_form(self, get_logger):
        log = get_logger
        log.info(
            "==== Verify checkout information form fields are displaying error message for empty data ===="
        )
        checkout_form_page = CheckoutFormPage(self.page)
        plp = ProductListPage(self.page)
        cart_page = CartPage(self.page)

        log.info("Step2: Add all the products to the cart")
        plp.add_all_products_to_cart()
        log.info('Step3: Navigate to "Cart" page')
        plp.click_cart_button()
        log.info("Step4: Click on 'Checkout' button")
        cart_page.click_checkout_button()
        log.info('Step5: Click on "Continue" button without filling the details')
        checkout_form_page.click_continue_btn()
        log.info("Verify error message is displayed")
        try:
            assert checkout_form_page.error_exists()
            error = checkout_form_page.get_error_msg()
            log.info('Verify error is dispalyed for "First Name"')
            assert "First Name" in error
            log.info(f"Error message is displyed. Error Msg: {error}")
        except AssertionError as e:
            log.error(
                f"Error message is not displayed for First Name or no message is displayed at all"
            )
            allure.attach(
                self.page.screenshot(),
                "evidence",
                attachment_type=AttachmentType.PNG,
            )
        log.info('Step6: Now Enter only "First Name"')
        checkout_form_page.enter_first_name("Swapnil")
        checkout_form_page.click_continue_btn()
        try:
            assert checkout_form_page.error_exists()
            error = checkout_form_page.get_error_msg()
            log.info('Verify error is displayed for "Last Name"')
            assert "Last Name" in error
            log.info(f"Error message is displayed. Error Msg: {error}")
        except AssertionError as e:
            log.error(
                f"Error message is not displayed for Last Name or no message is displayed at all"
            )
            allure.attach(
                self.page.screenshot(),
                "evidence",
                attachment_type=AttachmentType.PNG,
            )

        log.info('Step7: Now enter "First Name and Last Name"')
        # First name is already fill
        checkout_form_page.enter_last_name("Sonawane")
        checkout_form_page.click_continue_btn()
        try:
            assert checkout_form_page.error_exists()
            error = checkout_form_page.get_error_msg()
            log.info('Verify error is displayed for "Postal Code"')
            assert "Postal Code" in error
            log.info(f"Error message is displayed. Error Msg: {error}")
        except AssertionError as e:
            log.error(
                f"Error message is not displayed for Postal Code or no message is displayed at all"
            )
            allure.attach(
                self.page.screenshot(),
                "evidence",
                attachment_type=AttachmentType.PNG,
            )
        log.info("Step8: Now enter all the correct details and click on Submit button")
        checkout_form_page.enter_post_code("4455")
        checkout_form_page.click_continue_btn()
        log.info("Verify user is on Chcekout Overview page")
        try:
            assert (
                "Checkout: Overview"
                in checkout_form_page.get_chckout_overview_page_heading()
            )
            log.info("User is successfully navigated to checkout overview page")
            log.info("**** Test User Information Form Successful. ****")
        except AssertionError as e:
            log.error(f"User is not navigate to Checkout Overview page. Error: {e}")
            allure.attach(
                self.page.screenshot(),
                "evidence",
                attachment_type=AttachmentType.PNG,
            )
            log.info("**** Test User Information Form Failed. ****")
            pytest.fail()
            raise

    @pytest.mark.order(3)
    def test_cancel_button(self, get_logger):
        log = get_logger
        log.info(
            "==== Verify clicking on Cancel button user is redirected to Cart Page. ===="
        )
        checkout_form_page = CheckoutFormPage(self.page)
        plp = ProductListPage(self.page)
        cart_page = CartPage(self.page)

        log.info("Step2: Add all the products to the cart")
        plp.add_all_products_to_cart()
        log.info('Step3: Navigate to "Cart" page')
        plp.click_cart_button()
        log.info("Step4: Click on 'Checkout' button")
        cart_page.click_checkout_button()
        log.info("Step5: Click on Cancel button")
        checkout_form_page.click_cancel_btn()
        try:
            assert cart_page.is_cart_heading()
            log.info("user is navigated back to Cart page")
            log.info("**** Test Cancel Button Successful ****")
        except AssertionError as e:
            log.error(f"User is not navigate to Checkout Overview page. Error: {e}")
            allure.attach(
                self.page.screenshot(),
                "evidence",
                attachment_type=AttachmentType.PNG,
            )
            log.info("**** Test Cancel Button Failed ****")
            pytest.fail()
            raise

    @pytest.mark.order(4)
    def test_information_form_negative_data(self, get_logger):
        """Verify negative information in forms"""

        log = get_logger
        log.info(
            "Verify checkout information form fields are displaying error message for invalid data"
        )
        checkout_form_page = CheckoutFormPage(self.page)
        plp = ProductListPage(self.page)
        cart_page = CartPage(self.page)

        log.info("Step2: Add all the products to the cart")
        plp.add_all_products_to_cart()
        log.info('Step3: Navigate to "Cart" page')
        plp.click_cart_button()
        log.info("Step4: Click on 'Checkout' button")
        cart_page.click_checkout_button()

        log.info(
            "Step5: Now enter all the incorrect details and click on Submit button (Negative Data Test)"
        )
        checkout_form_page.enter_first_name("123")
        checkout_form_page.enter_last_name("456")
        checkout_form_page.enter_post_code("random")
        log.info("Verify user should not be able to proceed as invalid data is entered")
        try:
            checkout_form_page.click_continue_btn()
            # assert checkout_form_page.information_page_heading_exits()
            assert (
                "Checkout: Overview"
                not in checkout_form_page.get_chckout_overview_page_heading()
            )
            log.info("User is unable to proceed with invalid data")
            log.info("**** Test Information Form with Negative Data Successful ****")
        except AssertionError as e:
            log.error(f"User is navigate to Checkout Overview page. Error: {e}")
            allure.attach(
                self.page.screenshot(),
                "evidence",
                attachment_type=AttachmentType.PNG,
            )
            log.info("**** Test Information Form with Negative Data Failed ****")
            pytest.fail()
            raise
