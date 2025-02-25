from selenium.webdriver.common.by import By


def by_xpath_locator(locator: str) -> list[str]:
    return [By.XPATH, locator]


def by_class_locator(locator: str) -> list[str]:
    return [By.CLASS_NAME, locator]


BASE_BUTTON_LOCATOR = [By.CLASS_NAME, 'button_button__33qZ0']
RESTORE_PASSWORD_LOCATOR = [By.XPATH, ".//a[text()='Восстановить пароль']"]
EMAIL_INPUT_LOCATOR = [By.XPATH, "//label[text()='Email']/following-sibling::input"]
PERSONAL_ACCOUNT_BUTTON_LOCATOR = [By.XPATH, "//p[text()='Личный Кабинет']"]
CONSTRUCTOR_BUTTON_LOCATOR = [By.XPATH, "//p[text()='Конструктор']"]
BURGER_CONSTRUCTOR_LOCATOR = [By.XPATH, "//span[@class='constructor-element__row']"]
FEED_BUTTON_LOCATOR = [By.XPATH, "//p[text()='Лента Заказов']"]
MODAL_CLOSE_BUTTON_LOCATOR = [By.XPATH,
                              ".//button[@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"]
INGREDIENT_MODAL_LOCATOR = [By.XPATH, ".//section[contains(@class, 'Modal_modal__P3_V5')]"]
ALL_INGREDIENTS_TAB_LOCATOR = [By.XPATH, ".//div[contains(@class,'tab_tab__1SPyG')]"]
INGREDIENT_COUNTER_LOCATOR = ".//p[@class='counter_counter__num__3nue1']"
ORDER_NUMBER_LOCATOR = [By.XPATH,
                        ".//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8')]"]
CREATE_ORDER_BUTTON_LOCATOR = [By.XPATH,
                               ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']"]

ORDER_HISTORY = 'OrderHistory_link__1iNby'
ORDER_HISTORY_XPATH = f'.//a[@class=\'{ORDER_HISTORY}\']'

ORDER_LINK_LOCATOR = by_xpath_locator(ORDER_HISTORY_XPATH)

NOT_ACTIVE_INGREDIENT_LOCATOR = [By.XPATH, ".//a[@class = 'BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8']"]

ORDER_COUNTER_LOCATOR = [By.XPATH, ".//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']"]
WORKING_ORDER_LIST_LOCATOR = [By.XPATH, ".//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']"]
LIST_ITEM_LOCATOR = [By.XPATH, ".//li[@class = 'text text_type_digits-default mb-2']"]
MODAL_LOCATOR = [By.XPATH, ".//div[@class='Modal_modal_overlay__x2ZCr']"]
BUN_LOCATOR = [By.XPATH, ".//p[contains(text(), 'булка')]"]
