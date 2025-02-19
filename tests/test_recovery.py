import pytest
from selenium import webdriver

from conftest import setup_driver
from page_object.home_page import HomePage
from page_object.personal_account_page import PersonalAccountPage
from urls import FORGOT_PASSWORD


class TestPasswordRecovery:

    @pytest.mark.parametrize('driver', [webdriver.Chrome(), webdriver.Firefox()])
    def test_password_recovery(self, driver, setup_driver):
        home_page = HomePage(driver)
        home_page.click_account_button()
        account_page = PersonalAccountPage(driver)
        account_page.click_restore_button()
        assert driver.current_url == FORGOT_PASSWORD
