import allure

from locators.basic_functionality_locators import EMAIL_INPUT_LOCATOR
from locators.forgot_password_locators import RECOVER_PASSWORD_BUTTON_LOCATOR
from page_object.page import Page
from urls import FORGOT_PASSWORD_URL


class ForgotPasswordPage(Page):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Введение почты и нажатие восстановить")
    def enter_mail_and_click_recover(self):
        email_input = self.find_element_by_locator(EMAIL_INPUT_LOCATOR)
        email_input.send_keys('12345@mail.ru')
        self.find_and_click_element(RECOVER_PASSWORD_BUTTON_LOCATOR)

    @allure.step("Открытие страницы восстановления пароля")
    def open_page(self):
        self.driver.get(FORGOT_PASSWORD_URL)
