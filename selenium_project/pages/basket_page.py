import re

from .header_page import HeaderPage
from .locators import BasketPageLocators

class BasketPage(HeaderPage):
    def should_be_basket_page(self):
        self.__should_be_basket_url()

    def should_be_message_empty(self):
        assert self.is_element_with_text_present(*BasketPageLocators.MESSAGE_EMPTY,
                                                 "Ваша корзина пуста"), "Message about empty basket is not presented"
    def should_not_be_products(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT), \
            "Products are presented, but basket should be empty"

    def __should_be_basket_url(self):
        basket_url = re.compile(r'.*selenium1py\.pythonanywhere.com\/ru\/basket\/')
        assert self.is_url_correct(basket_url), "basket URL is not correct"