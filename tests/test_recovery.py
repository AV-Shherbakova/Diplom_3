import pytest
from selenium import webdriver

from conftest import setup_driver
from page_object.forgot_password_page import ForgotPasswordPage
from page_object.home_page import HomePage
from page_object.personal_account_page import PersonalAccountPage
from page_object.reset_password_page import ResetPasswordPage
from urls import FORGOT_PASSWORD_URL, RESET_PASSWORD_URL


class TestPasswordRecovery:

    @staticmethod
    def reset_password(driver):
        forgot_pass_page = ForgotPasswordPage(driver)
        forgot_pass_page.enter_mail_and_click_recover()
        assert driver.current_url == RESET_PASSWORD_URL

    @pytest.mark.parametrize('driver', [webdriver.Chrome(), webdriver.Firefox()])
    def test_password_recovery(self, driver, setup_driver):
        home_page = HomePage(driver)
        home_page.click_account_button()
        account_page = PersonalAccountPage(driver)
        account_page.click_restore_button()
        assert driver.current_url == FORGOT_PASSWORD_URL

    @pytest.mark.parametrize('driver', [webdriver.Chrome(), webdriver.Firefox()])
    def test_enter_mail_and_click_recovery(self, driver, setup_driver):
        self.reset_password(driver)

    @pytest.mark.parametrize('driver', [webdriver.Chrome(), webdriver.Firefox()])
    def test_reveal_password_click(self, driver, setup_driver):
        self.reset_password(driver)
        reset_page = ResetPasswordPage(driver)
        assert reset_page.click_password_reveal_and_return_changed()
