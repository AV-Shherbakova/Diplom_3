import allure

from locators.reset_password_locators import PASSWORD_INPUT_LOCATOR, PASSWORD_REVEAL_BUTTON
from page_object.page import Page

TYPE = 'type'


class ResetPasswordPage(Page):

    @allure.step("Нажатие на показать пароль")
    def click_password_reveal_and_return_changed(self) -> bool:
        password_input = self.find_element_by_locator(PASSWORD_INPUT_LOCATOR)
        init_type = password_input.get_attribute(TYPE)
        self.find_and_click_element(PASSWORD_REVEAL_BUTTON)
        return password_input.get_attribute(TYPE) != init_type
