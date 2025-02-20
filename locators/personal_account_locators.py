from selenium.webdriver.common.by import By

EMAIL_INPUT_LOCATOR = [By.XPATH, "//label[text()='Email']/following-sibling::input"]
PASSWORD_INPUT_LOCATOR = [By.XPATH, "//label[text()='Пароль']/following-sibling::input"]
ORDER_HISTORY_LOCATOR = [By.XPATH, "//a[text()='История заказов']"]
LOGOUT_LOCATOR = [By.XPATH, "//button[text()='Выход']"]
