import pytest
import time

from .pages.main_page import MainPage
from .pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

@pytest.mark.register
class TestRegisterOnLoginPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.email = str(time.time()) + "@fakemail.org"
        self.password = "QwErTy98761234"

    def test_guest_can_register(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_page()
        page.should_be_correct_fields_and_button_on_register_form()
        page.register(self.email, self.password)
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_main_page()
        main_page.should_be_authorized_user()
        main_page.should_be_success_register_message()