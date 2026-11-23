from allure_commons.types import AttachmentType
import pytest
import allure
from utilities.base_class import BaseClass
from PageObjects.login_page import LoginPage
from testData.user_credentials import UserCreds
from config.config import Config


class TestLoginPage(BaseClass):

    # Fixture
    @pytest.fixture(params=UserCreds().get_user_creds_data())
    def get_user_credentials(self, request):
        return request.param

    @pytest.fixture(params=UserCreds().get_user_creds_data())
    def get_invalid_credentials(self, request):
        return request.param

    @pytest.mark.skip
    def test_login(self, get_logger, setup_page, get_user_credentials):
        log = get_logger
        log.info(
            "Test Case Summary: Verify user is able to login to saucedemo website using valid credentials "
            "and Unable to login using Invalid credentials."
        )
        log.info(
            f"Login with username: {get_user_credentials["username"]} and password: {get_user_credentials["password"]}"
        )
        log.info("Step 1: Launch the website https://www.saucedemo.com")
        log.info("Launching the browser and navigated to https://www.saucedemo.com")
        log.info("Step2: Perform login")
        login_page = LoginPage(setup_page)
        login_page.login(
            username=get_user_credentials["username"],
            password=get_user_credentials["password"],
        )
        log.info(
            "Step 3: Verify user navigated to home page of Products and 'Products' title is displayed"
        )
        login_page.assert_url_contains(substring="inventory.html")
        try:
            assert login_page.title_exists()
            log.info("Products title exist, Login verification successful")
        except:
            log.error(
                "User is unable to login error displayed as: " + login_page.error_msg()
            )
            allure.attach(
                setup_page.screenshot(),
                "evidence",
                attachment_type=AttachmentType.PNG,
            )
            try:
                assert login_page.error_message_exists()
                log.info("error message is displayed : " + login_page.error_msg())
            except:
                log.error("Error message not displayed for invalid credentials")
                allure.attach(
                    setup_page.screenshot(),
                    "evidence",
                    attachment_type=AttachmentType.PNG,
                )
                pytest.fail("Error message for invalid credentials should be displayed")
            pytest.fail("User is unable to login error message displayed successfully")
        log.info("Closing the browser")

    @pytest.mark.negative
    @pytest.mark.skip
    def test_login_invlaid_creds(self, get_logger, setup_page, get_invalid_credentials):
        log = get_logger
        log.info(
            "Test Case Summary: Verify user is able to login to saucedemo website using valid credentials "
            "and Unable to login using Invalid credentials."
        )
        log.info(
            f"Login with username: {get_invalid_credentials["username"]} and password: {get_invalid_credentials["password"]}"
        )
        log.info("Step 1: Launch the website https://www.saucedemo.com")
        log.info("Launching the browser and navigated to https://www.saucedemo.com")
        log.info("Step2: Perform login")
        login_page = LoginPage(setup_page)
        login_page.login(
            username=get_invalid_credentials["username"],
            password=get_invalid_credentials["password"],
        )
        log.info(
            "Step 3: Verify user navigated to home page of Products and 'Products' title is displayed"
        )
        login_page.assert_url_contains(substring="inventory.html")
        try:
            assert login_page.title_exists()
            log.info("Products title exist, Login verification successful")
        except:
            log.error(
                "User is unable to login error displayed as: " + login_page.error_msg()
            )
            allure.attach(
                setup_page.screenshot(),
                "evidence",
                attachment_type=AttachmentType.PNG,
            )
            try:
                assert login_page.error_message_exists()
                log.info("error message is displayed : " + login_page.error_msg())
            except:
                log.error("Error message not displayed for invalid credentials")
                allure.attach(
                    setup_page.screenshot(),
                    "evidence",
                    attachment_type=AttachmentType.PNG,
                )
                pytest.fail("Error message for invalid credentials should be displayed")
            pytest.fail("User is unable to login error message displayed successfully")
        log.info("Closing the browser")

    @pytest.mark.positive
    def test_login_standard_user(self, get_logger, setup_page):
        log = get_logger
        log.info(
            "Test Case Summary: Verify user is able to login to saucedemo website using valid credentials "
            "and Unable to login using Invalid credentials."
        )
        log.info(
            f"Login with username: {Config.STANDARD_USER} and password: {Config.PASSWORD}"
        )
        log.info("Step 1: Launch the website https://www.saucedemo.com")
        log.info("Launching the browser and navigated to https://www.saucedemo.com")
        log.info("Step2: Perform login")
        login_page = LoginPage(setup_page)
        login_page.login(
            username=Config.STANDARD_USER,
            password=Config.PASSWORD,
        )
        log.info(
            "Step 3: Verify user navigated to home page of Products and 'Products' title is displayed"
        )
        login_page.assert_url_contains(substring="inventory.html")
        log.info(f"Current Page URL: {setup_page.url} or {login_page.get_url()}")
        try:
            assert login_page.title_exists()
            log.info(f"Login Successful for ====> {Config.STANDARD_USER}!!")
        except:
            log.error(
                "User is unable to login error displayed as: " + login_page.error_msg()
            )
            allure.attach(
                setup_page.screenshot(),
                "evidence",
                attachment_type=AttachmentType.PNG,
            )
            pytest.fail("User is unable to login error message displayed successfully")
        log.info("Closing the browser")

    @pytest.mark.positive
    def test_login_problem_user(self, get_logger, setup_page):
        log = get_logger
        log.info(
            "Test Case Summary: Verify user is able to login to saucedemo website using valid credentials "
            "and Unable to login using Invalid credentials."
        )
        log.info(
            f"Login with username: {Config.PROBLEM_USER} and password: {Config.PASSWORD}"
        )
        log.info("Step 1: Launch the website https://www.saucedemo.com")
        log.info("Launching the browser and navigated to https://www.saucedemo.com")
        log.info("Step2: Perform login")
        login_page = LoginPage(setup_page)
        login_page.login(
            username=Config.PROBLEM_USER,
            password=Config.PASSWORD,
        )
        log.info(
            "Step 3: Verify user navigated to home page of Products and 'Products' title is displayed"
        )
        log.info(f"Current Page URL: {setup_page.url} or {login_page.get_url()}")
        try:
            assert login_page.title_exists()
            log.info(f"Login Successful for ====> {Config.PROBLEM_USER} !!")
        except:
            log.error(
                "User is unable to login error displayed as: " + login_page.error_msg()
            )
            allure.attach(
                setup_page.screenshot(),
                "evidence",
                attachment_type=AttachmentType.PNG,
            )
            pytest.fail("User is unable to login error message displayed successfully")
        log.info("Closing the browser")

    @pytest.mark.negative
    def test_login_locked_user(self, get_logger, setup_page):
        log = get_logger
        log.info(
            "Test Case Summary: Verify user is able to login to saucedemo website using valid credentials "
            "and Unable to login using Invalid credentials."
        )
        log.info(
            f"Login with username: {Config.LOCKED_OUT_USER} and password: {Config.PASSWORD}"
        )
        log.info("Step 1: Launch the website https://www.saucedemo.com")
        log.info("Launching the browser and navigated to https://www.saucedemo.com")
        log.info("Step2: Perform login")
        login_page = LoginPage(setup_page)
        login_page.login(
            username=Config.LOCKED_OUT_USER,
            password=Config.PASSWORD,
        )
        log.info(
            "Step 3: Verify user navigated to home page of Products and 'Products' title is displayed"
        )
        try:
            assert login_page.title_exists()
            log.info(f"Login Successful for ====> {Config.LOCKED_OUT_USER} !!")
        except:
            log.error(
                "User is unable to login error displayed as: " + login_page.error_msg()
            )
            allure.attach(
                setup_page.screenshot(),
                "evidence",
                attachment_type=AttachmentType.PNG,
            )
            pytest.fail("User is unable to login error message displayed successfully")
        log.info("Closing the browser")

    @pytest.mark.positive
    def test_login_performance_glitch_user(self, get_logger, setup_page):
        log = get_logger
        log.info(
            "Test Case Summary: Verify user is able to login to saucedemo website using valid credentials "
            "and Unable to login using Invalid credentials."
        )
        log.info(
            f"Login with username: {Config.PERFORMANCE_GLITCH_USER} and password: {Config.PASSWORD}"
        )
        log.info("Step 1: Launch the website https://www.saucedemo.com")
        log.info("Launching the browser and navigated to https://www.saucedemo.com")
        log.info("Step2: Perform login")
        login_page = LoginPage(setup_page)
        login_page.login(
            username=Config.PERFORMANCE_GLITCH_USER,
            password=Config.PASSWORD,
        )
        log.info(
            "Step 3: Verify user navigated to home page of Products and 'Products' title is displayed"
        )
        login_page.assert_url_contains(substring="inventory.html")
        log.info(f"Current Page URL: {setup_page.url} or {login_page.get_url()}")
        try:
            assert login_page.title_exists()
            log.info(f"Login Successful for ====> {Config.PERFORMANCE_GLITCH_USER} !!")
        except:
            log.error(
                "User is unable to login error displayed as: " + login_page.error_msg()
            )
            allure.attach(
                setup_page.screenshot(),
                "evidence",
                attachment_type=AttachmentType.PNG,
            )
            pytest.fail("User is unable to login error message displayed successfully")
        log.info("Closing the browser")
