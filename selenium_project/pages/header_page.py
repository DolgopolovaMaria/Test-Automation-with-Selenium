from .base_page import BasePage
from .locators import HeaderPageLocators

class HeaderPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element(*HeaderPageLocators.LOGIN_LINK)
        link.click()

    def go_to_basket_page(self):
        link = self.browser.find_element(*HeaderPageLocators.BASKET_LINK)
        link.click()

    def go_to_main_page(self):
        link = self.browser.find_element(*HeaderPageLocators.MAIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*HeaderPageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_authorized_user(self):
        assert self.is_element_present(*HeaderPageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"