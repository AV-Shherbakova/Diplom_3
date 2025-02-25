import allure

from conftest import driver
from page_object.forgot_password_page import ForgotPasswordPage
from page_object.home_page import HomePage
from page_object.personal_account_page import PersonalAccountPage
from page_object.reset_password_page import ResetPasswordPage
from urls import FORGOT_PASSWORD_URL, RESET_PASSWORD_URL


class TestPasswordRecovery:

    @allure.title("Проверка восстановления пароля")
    def test_password_recovery(self, driver):
        home_page = HomePage(driver)
        home_page.click_account_button()
        account_page = PersonalAccountPage(driver)
        account_page.click_restore_button()
        url_changed = account_page.url_changed(FORGOT_PASSWORD_URL)
        assert url_changed is True

    @allure.title("Проверка ввода почты и нажатия восстановить пароль")
    def test_enter_mail_and_click_recovery(self, driver):
        forgot_pass_page = ForgotPasswordPage(driver)
        forgot_pass_page.open_page()
        forgot_pass_page.enter_mail_and_click_recover()
        url_changed = forgot_pass_page.url_changed(RESET_PASSWORD_URL)
        assert url_changed is True

    @allure.title("Проверка видимости пароля по клику")
    def test_reveal_password_click(self, driver):
        forgot_pass_page = ForgotPasswordPage(driver)
        forgot_pass_page.open_page()
        forgot_pass_page.enter_mail_and_click_recover()
        reset_page = ResetPasswordPage(driver)
        assert reset_page.click_password_reveal_and_return_changed()
