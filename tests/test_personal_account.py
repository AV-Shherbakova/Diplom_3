import pytest
from selenium import webdriver

from conftest import setup_driver, create_and_remove_user
from constants import PASSWORD
from page_object.home_page import HomePage
from page_object.personal_account_page import PersonalAccountPage
from urls import ACCOUNT_URL, ORDER_HISTORY_URL, LOGIN_URL


class TestPersonalAccount:

    @pytest.mark.parametrize('driver', [webdriver.Chrome()])
    def test_personal_account_page_open(self, driver, setup_driver, create_and_remove_user):
        home_page = HomePage(driver)
        home_page.click_account_button()
        account_page = PersonalAccountPage(driver)
        email = create_and_remove_user.json().get('user').get('email')
        account_page.sign_in(email, PASSWORD)
        account_page.click_personal_account()
        assert driver.current_url == ACCOUNT_URL

    @pytest.mark.parametrize('driver', [webdriver.Chrome()])
    def test_order_history_open(self, driver, setup_driver, create_and_remove_user):
        home_page = HomePage(driver)
        home_page.click_account_button()
        account_page = PersonalAccountPage(driver)
        email = create_and_remove_user.json().get('user').get('email')
        account_page.sign_in(email, PASSWORD)
        account_page.click_personal_account()
        account_page.click_order_history()
        assert driver.current_url == ORDER_HISTORY_URL

    @pytest.mark.parametrize('driver', [webdriver.Chrome()])
    def test_logout(self, driver, setup_driver, create_and_remove_user):
        home_page = HomePage(driver)
        home_page.click_account_button()
        account_page = PersonalAccountPage(driver)
        email = create_and_remove_user.json().get('user').get('email')
        account_page.sign_in(email, PASSWORD)
        account_page.click_personal_account()
        account_page.click_logout()
        assert driver.current_url == LOGIN_URL
