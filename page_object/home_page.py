import allure

from constants import HREF
from locators.basic_functionality_locators import *
from page_object.page import Page
from utils import get_random_index_from_list


class HomePage(Page):

    @allure.step("Нажатие на кнопку Личный кабинет")
    def click_account_button(self):
        self.find_and_click_element(PERSONAL_ACCOUNT_BUTTON_LOCATOR)

    @allure.step("Открытие Конструктора")
    def click_constructor_button(self):
        self.find_and_click_element(CONSTRUCTOR_BUTTON_LOCATOR)

    @allure.step("Открытие Ленты Заказов")
    def click_feed_button(self):
        self.find_and_click_element(FEED_BUTTON_LOCATOR)

    @allure.step("Нажатие на рандомный ингредиент и возврат ссылки на него")
    def click_random_ingredient_and_return_ref(self) -> str:
        ingredients = self.find_elements_by_locator(NOT_ACTIVE_INGREDIENT_LOCATOR)
        idx = get_random_index_from_list(ingredients)
        ingredient = ingredients[idx]
        ingredient.click()
        return ingredient.get_attribute(HREF)

    @allure.step("Закрытие модального окна")
    def close_modal(self):
        self.find_and_click_element(MODAL_CLOSE_BUTTON_LOCATOR)

    @allure.step("Проверка открыто ли модальное окно ингредиента")
    def get_ingredient_modal_opened(self) -> bool:
        ingredient_modal = self.find_element_by_locator(INGREDIENT_MODAL_LOCATOR)
        return "opened" in ingredient_modal.get_attribute('class')

    @allure.step("Добавление ингредиента и возврат значения счётчика")
    def add_ingredient_and_return_counter(self):
        ingredients = self.find_elements_by_locator(NOT_ACTIVE_INGREDIENT_LOCATOR)
        idx = get_random_index_from_list(ingredients)
        ingredient = ingredients[idx]
        basket_constructor = self.find_element_by_locator(BURGER_CONSTRUCTOR_LOCATOR)
        self.drag_and_drop(ingredient, basket_constructor)
        counter = ingredient.find_element(By.XPATH, INGREDIENT_COUNTER_LOCATOR)
        return int(counter.text)

    @allure.step("Создание дефолтного заказа из 2-х булок")
    def create_default_ingredient_order(self):
        default_ingredient = self.find_element_by_locator(BUN_LOCATOR)
        basket_constructor = self.find_element_by_locator(BURGER_CONSTRUCTOR_LOCATOR)
        self.drag_and_drop(default_ingredient, basket_constructor)
        self.wait_for_element_invisible(MODAL_LOCATOR)

    @allure.step("Нажатие кнопки оформить заказ")
    def click_create_order_button(self):
        self.find_and_click_element(CREATE_ORDER_BUTTON_LOCATOR)
        self.wait_for_element_visible(ORDER_NUMBER_LOCATOR)

    @allure.step("Возврат результата изменения номера заказа")
    def order_number_changed(self):
        self.wait_for_element_visible(ORDER_NUMBER_LOCATOR)
        return self.wait_element_changed_text(ORDER_NUMBER_LOCATOR, "9999")

    @allure.step("Нажатие на заказ и возврат ссылки на него")
    def click_order_item_and_return_ref(self):
        order_items = self.find_elements_by_locator(ORDER_LINK_LOCATOR)
        idx = get_random_index_from_list(order_items)
        order_item = order_items[idx]
        order_item.click()
        return order_item.get_attribute(HREF)

    @allure.step("Получение ссылки на последний созданный заказ")
    def get_last_feed_order_ref(self):
        return self.find_elements_by_locator(ORDER_LINK_LOCATOR)[0].get_attribute(HREF)

    @allure.step("Получение количества заказов за всё время")
    def get_total_order_count(self):
        return self.get_total_counter(False)

    @allure.step("Получение количества заказов за сегодня")
    def get_daily_order_count(self):
        return self.get_total_counter(True)

    @allure.step("Получение количества заказов")
    def get_total_counter(self, daily: bool):
        idx = 1 if daily else 0
        counter = self.find_elements_by_locator(ORDER_COUNTER_LOCATOR)[idx].text
        return int(counter)

    @allure.step("Получение изменения последнего заказа в работе")
    def get_last_working_order_appeared(self, expected_order_number) -> bool:
        return self.get_text_become_expected(LIST_ITEM_LOCATOR, f"0{expected_order_number}")
