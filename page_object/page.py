import time


class Page:

    def __init__(self, driver):
        self.driver = driver

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def find_element_by_locator(self, locator):
        return self.driver.find_element(*locator)

    def find_elements_by_locator(self, locator):
        return self.driver.find_elements(*locator)

    def click_element(self, element):
        element.click()

    def find_and_click_element(self, locator):
        self.click_element(self.find_element_by_locator(locator))

    def wait(self):
        time.sleep(0.5)
