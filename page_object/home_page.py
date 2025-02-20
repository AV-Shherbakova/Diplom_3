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
        return ingredient.get_attribute('href')

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
