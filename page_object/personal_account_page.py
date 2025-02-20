from locators.basic_functionality_locators import RESTORE_PASSWORD_LOCATOR, BASE_BUTTON_LOCATOR, \
    PERSONAL_ACCOUNT_BUTTON_LOCATOR
from locators.personal_account_locators import PASSWORD_INPUT_LOCATOR, EMAIL_INPUT_LOCATOR, \
    ORDER_HISTORY_LOCATOR, LOGOUT_LOCATOR
from page_object.page import Page


class PersonalAccountPage(Page):

    def click_restore_button(self):
        self.find_and_click_element(RESTORE_PASSWORD_LOCATOR)

    def sign_in(self, email, password):
        self.find_element_by_locator(EMAIL_INPUT_LOCATOR).send_keys(email)
        self.find_element_by_locator(PASSWORD_INPUT_LOCATOR).send_keys(password)
        self.find_and_click_element(BASE_BUTTON_LOCATOR)
        self.wait()

    def click_personal_account(self):
        self.find_and_click_element(PERSONAL_ACCOUNT_BUTTON_LOCATOR)
        self.wait()

    def click_order_history(self):
        self.find_and_click_element(ORDER_HISTORY_LOCATOR)
        self.wait()

    def click_logout(self):
        self.find_and_click_element(LOGOUT_LOCATOR)
        self.wait()
