import math
from selenium.webdriver.common.by import By

from .locators import ProductPageLocators
from .header_page import HeaderPage

class ProductPage(HeaderPage):

    def add_product_to_basket(self):
        button_add = self.browser.find_element(*ProductPageLocators.BUTTON_ADD)
        button_add.click()

    def should_be_added_product(self):
        self.__should_be_message_add()
        self.__should_be_message_price()
        product_name = self.__get_product_name()
        self.__should_be_correct_message_text(product_name)
        price = self.__get_product_price()
        self.__should_be_correct_price(price)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ADD), \
            "Success message is presented, but should not be"

    def should_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ADD), \
            "Success message is not disappeared"

    def __should_be_message_add(self):
        assert self.is_element_with_text_present(*ProductPageLocators.MESSAGE_ADD, "добавлен в вашу корзину"), "Message about adding is not presented"

    def __should_be_message_price(self):
        assert self.is_element_with_text_present(*ProductPageLocators.MESSAGE_PRICE, "Стоимость корзины теперь составляет"), "Message about price is not presented"

    def __should_be_correct_message_text(self, product_name):
        message = self.find_element_with_text(*ProductPageLocators.MESSAGE_ADD, "добавлен в вашу корзину")
        message_text = message.text
        correct_message_text = f"{product_name} был добавлен в вашу корзину."
        assert correct_message_text in message_text, f"Invalid message after adding: expect '{correct_message_text}', get '{message_text}'"

    def __should_be_correct_price(self, price):
        message = self.find_element_with_text(*ProductPageLocators.MESSAGE_PRICE, "Стоимость корзины теперь составляет")
        message_text = message.text
        assert price in message_text, "Message after adding: invalid price"

    def __get_product_name(self):
        e = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        e_text = e.text
        return e_text

    def __get_product_price(self):
        e = self.browser.find_element(*ProductPageLocators.PRICE)
        e_text = e.text
        return e_text

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")