import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10, 0.01)

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Получение элемента по локатору")
    def find_element_by_locator(self, locator):
        self.wait_for_element_to_appear(locator)
        return self.driver.find_element(*locator)

    def find_elements_by_locator(self, locator) -> list:
        self.wait_for_element_to_appear(locator)
        return self.driver.find_elements(*locator)

    def drag_and_drop(self, element_from, element_to):
        js_code = """
            const source = arguments[0];
            const target = arguments[1];
            const dataTransfer = new DataTransfer();

            source.dispatchEvent(new DragEvent('dragstart', { bubbles: true, cancelable: true, dataTransfer }));
            target.dispatchEvent(new DragEvent('drop', { bubbles: true, cancelable: true, dataTransfer }));
            source.dispatchEvent(new DragEvent('dragend', { bubbles: true, cancelable: true, dataTransfer }));
        """
        self.driver.execute_script(js_code, element_from, element_to)

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url

    def find_and_click_element(self, locator):
        self.wait_for_element_to_appear(locator)
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def wait_for_element_to_appear(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_invisible(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))

    def wait_element_changed_text(self, locator, expected_text) -> bool:
        return self.wait.until(lambda d: d.find_element(*locator).text.strip() != expected_text)

    def get_text_become_expected(self, locator, expected_text: str):
        return self.wait.until(lambda d: d.find_element(*locator).text.strip() == expected_text)

    @allure.step("Ожидание смены URL")
    def url_changed(self, url):
        return self.wait.until(lambda d: d.current_url == url)
