import allure

from conftest import driver, create_and_remove_user
from constants import PASSWORD
from page_object.home_page import HomePage
from page_object.personal_account_page import PersonalAccountPage
from urls import FEED_URL, BASE_URL


class TestBaseFunctions:

    @allure.title("Проверка нажатия на Ленту Заказов")
    def test_feed_click(self, driver):
        home_page = HomePage(driver)
        home_page.click_feed_button()
        assert home_page.get_current_url() == FEED_URL

    @allure.title("Проверка нажатия на Конструктор")
    def test_constructor_click(self, driver):
        home_page = HomePage(driver)
        home_page.click_feed_button()
        assert home_page.get_current_url() == FEED_URL
        home_page.click_constructor_button()
        assert home_page.get_current_url() == BASE_URL + '/'

    @allure.title("Проверка нажатия на ингредиент")
    def test_ingredient_click(self, driver):
        home_page = HomePage(driver)
        link = home_page.click_random_ingredient_and_return_ref()
        assert home_page.get_current_url() == link

    @allure.title("Проверка закрытия модального окна ингредиента")
    def test_close_modal_click(self, driver):
        home_page = HomePage(driver)
        home_page.click_random_ingredient_and_return_ref()
        assert home_page.get_ingredient_modal_opened() == True
        home_page.close_modal()
        assert home_page.get_ingredient_modal_opened() == False

    @allure.title("Проверка увеличения количества ингредиентов")
    def test_increase_ingredient_counter(self, driver):
        home_page = HomePage(driver)
        counter = home_page.add_ingredient_and_return_counter()
        assert counter > 0

    @allure.title("Проверка создания заказа")
    def test_create_order(self, driver, create_and_remove_user):
        home_page = HomePage(driver)
        home_page.click_account_button()
        account_page = PersonalAccountPage(driver)
        email = create_and_remove_user.json().get('user').get('email')
        account_page.sign_in(email, PASSWORD)
        home_page.create_default_ingredient_order()
        home_page.click_create_order_button()
        text_changed = home_page.order_number_changed()
        assert text_changed
