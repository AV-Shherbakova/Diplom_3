import allure

from conftest import driver, create_and_remove_user
from constants import PASSWORD
from page_object.home_page import HomePage
from page_object.personal_account_page import PersonalAccountPage
from utils import create_order_and_get_field, ID


class TestOrders:

    @allure.title("Проверка открытия заказа в ленте")
    def test_open_order_in_feed(self, driver):
        home_page = HomePage(driver)
        home_page.click_feed_button()
        link = home_page.click_order_item_and_return_ref()
        assert home_page.get_current_url() == link

    @allure.title("Проверка, что заказ из истории появился в ленте заказов")
    def test_order_from_history_in_feed(self, driver, create_and_remove_user):
        home_page = HomePage(driver)
        home_page.click_account_button()
        account_page = PersonalAccountPage(driver)
        email = create_and_remove_user.json().get('user').get('email')
        account_page.sign_in(email, PASSWORD)
        order_id = create_order_and_get_field(create_and_remove_user, ID)
        account_page.click_personal_account()
        account_page.click_order_history()
        last_account_order_ref = account_page.get_last_order_ref()
        home_page.click_feed_button()
        last_feed_order_ref = home_page.get_last_feed_order_ref()
        assert order_id in last_account_order_ref and order_id in last_feed_order_ref

    @allure.title("Проверка увеличения счётчика заказов за сегодня")
    def test_create_order_and_check_daily_counter_increase(self, driver, create_and_remove_user):
        home_page = HomePage(driver)
        home_page.click_feed_button()
        init_count = home_page.get_daily_order_count()
        create_order_and_get_field(create_and_remove_user, ID)
        assert init_count < home_page.get_daily_order_count()

    @allure.title("Проверка увеличения общего счётчика заказов")
    def test_create_order_and_check_total_counter_increase(self, driver, create_and_remove_user):
        home_page = HomePage(driver)
        home_page.click_feed_button()
        init_count = home_page.get_total_order_count()
        create_order_and_get_field(create_and_remove_user, ID)
        assert init_count < home_page.get_total_order_count()

    @allure.title("Проверка наличия номера созданного заказа в списке заказов")
    def test_order_number_in_order_list(self, driver, create_and_remove_user):
        home_page = HomePage(driver)
        home_page.click_feed_button()
        create_order_number = create_order_and_get_field(create_and_remove_user, "number")
        order_appeared = home_page.get_last_working_order_appeared(create_order_number)
        assert order_appeared is True
