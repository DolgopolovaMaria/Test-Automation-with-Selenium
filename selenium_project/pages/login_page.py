import re

from .header_page import HeaderPage
from .locators import LoginPageLocators

class LoginPage(HeaderPage):
    def should_be_login_page(self):
        self.__should_be_login_url()
        self.__should_be_login_form()
        self.__should_be_register_form()

    def should_be_correct_fields_and_button_on_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_LOGIN), "Login field on Register form is not presented"
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_PASSWORD), "Password field on Register for is not presented"
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_PASSWORD_2), "Confirm password field on Register for is not presented"
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_BUTTON), "Button on Register for is not presented"

    def register(self, email, password):
        login = self.browser.find_element(*LoginPageLocators.REGISTER_LOGIN)
        password_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        password_2_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_2)
        login.send_keys(email)
        password_field.send_keys(password)
        password_2_field.send_keys(password)

        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()

    def __should_be_login_url(self):
        login_url = re.compile(r'.*selenium1py\.pythonanywhere\.com\/ru\/accounts\/login\/')
        assert self.is_url_correct(login_url), "login URL is not correct"

    def __should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def __should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

