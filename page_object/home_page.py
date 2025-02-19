from locators.basic_functionality_locators import ACCOUNT_BUTTON_LOCATOR
from page_object.page import Page


class HomePage(Page):

    def click_account_button(self):
        self.find_and_click_element(ACCOUNT_BUTTON_LOCATOR)
