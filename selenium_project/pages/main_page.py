from selenium.webdriver.common.by import By
import re

from .header_page import HeaderPage
from .locators import MainPageLocators

class MainPage(HeaderPage):
    def should_be_main_page(self):
        self.__should_be_main_url()

    def should_be_success_register_message(self):
        assert self.is_element_present(*MainPageLocators.SUCCESS_REGISTER_MESSAGE), "Message about register is not presented"

    def __should_be_main_url(self):
        login_url = re.compile(r'.*selenium1py\.pythonanywhere\.com\/ru\/')
        assert self.is_url_correct(login_url), "login URL is not correct"