import time

from selenium.webdriver import ActionChains


class Page:

    def __init__(self, driver):
        self.driver = driver

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def find_element_by_locator(self, locator):
        return self.driver.find_element(*locator)

    def find_elements_by_locator(self, locator) -> list:
        return self.driver.find_elements(*locator)

    def drag_and_drop(self, element_from, element_to):
        ActionChains(self.driver).drag_and_drop(element_from, element_to).perform()

    @staticmethod
    def click_element(element):
        element.click()

    def find_and_click_element(self, locator):
        self.click_element(self.find_element_by_locator(locator))

    @staticmethod
    def wait():
        time.sleep(1)
