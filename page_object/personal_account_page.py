from locators.basic_functionality_locators import RESTORE_PASSWORD_LOCATOR
from page_object.page import Page


class PersonalAccountPage(Page):

    def click_restore_button(self):
        self.find_and_click_element(RESTORE_PASSWORD_LOCATOR)
