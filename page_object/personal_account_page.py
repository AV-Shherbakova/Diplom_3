import allure

from constants import HREF
from locators.basic_functionality_locators import *
from locators.personal_account_locators import *
from page_object.page import Page


class PersonalAccountPage(Page):

    @allure.step("Нажатие кнопку восстановления пароля")
    def click_restore_button(self):
        self.find_and_click_element(RESTORE_PASSWORD_LOCATOR)

    @allure.step("Проведение авторизации")
    def sign_in(self, email, password):
        self.find_element_by_locator(EMAIL_INPUT_LOCATOR).send_keys(email)
        self.find_element_by_locator(PASSWORD_INPUT_LOCATOR).send_keys(password)
        self.find_and_click_element(BASE_BUTTON_LOCATOR)

    @allure.step("Переход в личный кабинет")
    def click_personal_account(self):
        self.find_and_click_element(PERSONAL_ACCOUNT_BUTTON_LOCATOR)

    @allure.step("Переход в историю заказов")
    def click_order_history(self):
        self.find_and_click_element(ORDER_HISTORY_LOCATOR)

    @allure.step("Выход из личного кабинета")
    def click_logout(self):
        self.find_and_click_element(LOGOUT_LOCATOR)

    @allure.step("Получение ссылки на последний заказ")
    def get_last_order_ref(self):
        return self.find_elements_by_locator(ORDER_LINK_LOCATOR)[0].get_attribute(HREF)
