import time

import pytest
from selenium import webdriver

from conftest import setup_driver, create_and_remove_user
from constants import PASSWORD
from page_object.home_page import HomePage
from page_object.personal_account_page import PersonalAccountPage
from urls import FEED_URL, BASE_URL


class TestBaseFunctions:

    @pytest.mark.parametrize('driver', [webdriver.Chrome(), webdriver.Firefox()])
    def test_feed_click(self, driver, setup_driver):
        home_page = HomePage(driver)
        home_page.click_feed_button()
        assert driver.current_url == FEED_URL

    @pytest.mark.parametrize('driver', [webdriver.Chrome(), webdriver.Firefox()])
    def test_constructor_click(self, driver, setup_driver):
        home_page = HomePage(driver)
        home_page.click_feed_button()
        assert driver.current_url == FEED_URL
        home_page.click_constructor_button()
        assert driver.current_url == BASE_URL + '/'

    @pytest.mark.parametrize('driver', [webdriver.Chrome(), webdriver.Firefox()])
    def test_ingredient_click(self, driver, setup_driver):
        home_page = HomePage(driver)
        link = home_page.click_random_ingredient_and_return_ref()
        assert driver.current_url == link

    @pytest.mark.parametrize('driver', [webdriver.Chrome(), webdriver.Firefox()])
    def test_close_modal_click(self, driver, setup_driver):
        home_page = HomePage(driver)
        home_page.click_random_ingredient_and_return_ref()
        assert home_page.get_ingredient_model_opened() == True
        home_page.close_modal()
        assert home_page.get_ingredient_model_opened() == False

    @pytest.mark.parametrize('driver', [webdriver.Chrome(), webdriver.Firefox()])
    def test_increase_ingredient_counter(self, driver, setup_driver):
        home_page = HomePage(driver)
        assert home_page.add_ingredient_and_return_counter() > 0

    @pytest.mark.parametrize('driver', [webdriver.Chrome(), webdriver.Firefox()])
    def test_create_order(self, driver, setup_driver, create_and_remove_user):
        home_page = HomePage(driver)
        home_page.click_account_button()
        account_page = PersonalAccountPage(driver)
        email = create_and_remove_user.json().get('user').get('email')
        account_page.sign_in(email, PASSWORD)
        home_page.create_default_ingredient_order()
        home_page.click_create_order_button()
        time.sleep(5)
        order_number = home_page.get_order_number()
        assert order_number != 9999
