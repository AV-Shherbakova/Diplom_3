import allure

from conftest import driver, create_and_remove_user
from constants import PASSWORD
from page_object.home_page import HomePage
from page_object.personal_account_page import PersonalAccountPage
from urls import ACCOUNT_URL, ORDER_HISTORY_URL, LOGIN_URL


class TestPersonalAccount:

    @allure.title("Проверка открытия личного кабинета")
    def test_personal_account_page_open(self, create_and_remove_user, driver):
        home_page = HomePage(driver)
        home_page.click_account_button()
        account_page = PersonalAccountPage(driver)
        email = create_and_remove_user.json().get('user').get('email')
        account_page.sign_in(email, PASSWORD)
        account_page.click_personal_account()
        changed = account_page.url_changed(ACCOUNT_URL)
        assert changed is True

    @allure.title("Проверка открытия истории заказов")
    def test_order_history_open(self, driver, create_and_remove_user):
        home_page = HomePage(driver)
        home_page.click_account_button()
        account_page = PersonalAccountPage(driver)
        email = create_and_remove_user.json().get('user').get('email')
        account_page.sign_in(email, PASSWORD)
        account_page.click_personal_account()
        account_page.click_order_history()
        changed = account_page.url_changed(ORDER_HISTORY_URL)
        assert changed is True

    @allure.title("Проверка разлогина")
    def test_logout(self, driver, create_and_remove_user):
        home_page = HomePage(driver)
        home_page.click_account_button()
        account_page = PersonalAccountPage(driver)
        email = create_and_remove_user.json().get('user').get('email')
        account_page.sign_in(email, PASSWORD)
        account_page.click_personal_account()
        account_page.click_logout()
        changed = account_page.url_changed(LOGIN_URL)
        assert changed is True
