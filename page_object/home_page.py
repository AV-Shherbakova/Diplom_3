from constants import HREF
from locators.basic_functionality_locators import *
from page_object.page import Page
from utils import get_random_index_from_list


class HomePage(Page):

    def click_account_button(self):
        self.find_and_click_element(PERSONAL_ACCOUNT_BUTTON_LOCATOR)
        self.wait()

    def click_constructor_button(self):
        self.find_and_click_element(CONSTRUCTOR_BUTTON_LOCATOR)
        self.wait()

    def click_feed_button(self):
        self.find_and_click_element(FEED_BUTTON_LOCATOR)
        self.wait()

    def click_random_ingredient_and_return_ref(self) -> str:
        ingredients = self.find_elements_by_locator(NOT_ACTIVE_INGREDIENT_LOCATOR)
        idx = get_random_index_from_list(ingredients)
        ingredient = ingredients[idx]
        ingredient.click()
        self.wait()
        return ingredient.get_attribute(HREF)

    def close_modal(self):
        self.find_and_click_element(MODAL_CLOSE_BUTTON_LOCATOR)
        self.wait()

    def get_ingredient_model_opened(self) -> bool:
        self.wait()
        ingredient_modal = self.find_element_by_locator(INGREDIENT_MODAL_LOCATOR)
        return "opened" in ingredient_modal.get_attribute('class')

    def add_ingredient_and_return_counter(self):
        ingredients = self.find_elements_by_locator(NOT_ACTIVE_INGREDIENT_LOCATOR)
        idx = get_random_index_from_list(ingredients)
        ingredient = ingredients[idx]
        basket_constructor = self.find_element_by_locator(BURGER_CONSTRUCTOR_LOCATOR)
        self.drag_and_drop(ingredient, basket_constructor)
        self.wait()
        counter = ingredient.find_element(By.XPATH, INGREDIENT_COUNTER_LOCATOR)
        return int(counter.text)

    def create_default_ingredient_order(self):
        ingredients = self.find_elements_by_locator(NOT_ACTIVE_INGREDIENT_LOCATOR)
        default_ingredient = ingredients[0]
        basket_constructor = self.find_element_by_locator(BURGER_CONSTRUCTOR_LOCATOR)
        self.drag_and_drop(default_ingredient, basket_constructor)
        self.wait()

    def click_create_order_button(self):
        self.find_and_click_element(CREATE_ORDER_BUTTON_LOCATOR)

    def get_order_number(self):
        number_element = self.find_element_by_locator(ORDER_NUMBER_LOCATOR)
        return int(number_element.text)

    def click_order_item_and_return_ref(self):
        order_items = self.find_elements_by_locator(ORDER_LINK_LOCATOR)
        idx = get_random_index_from_list(order_items)
        order_item = order_items[idx]
        order_item.click()
        self.wait()
        return order_item.get_attribute(HREF)

    def get_last_feed_order_ref(self):
        return self.find_elements_by_locator(ORDER_LINK_LOCATOR)[0].get_attribute(HREF)

    def get_total_order_count(self):
        return self.get_total_counter(False)

    def get_daily_order_count(self):
        return self.get_total_counter(True)

    def get_total_counter(self, daily: bool):
        idx = 1 if daily else 0
        counter = self.find_elements_by_locator(ORDER_COUNTER_LOCATOR)[idx].text
        return int(counter)

    def get_last_working_order_number(self) -> int:
        order_list = self.find_element_by_locator(WORKING_ORDER_LIST_LOCATOR)
        new_order = order_list.find_elements(By.XPATH, LIST_ITEM_LOCATOR)[0]
        return int(new_order.text)
