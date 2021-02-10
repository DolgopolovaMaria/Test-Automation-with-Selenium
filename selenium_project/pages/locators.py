from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_LOGIN = (By.ID, "id_registration-email")
    REGISTER_PASSWORD = (By.ID, "id_registration-password1")
    REGISTER_PASSWORD_2 = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")

class ProductPageLocators():
    BUTTON_ADD = (By.CLASS_NAME, "btn-add-to-basket")
    MESSAGE_ADD = (By.CSS_SELECTOR, "#messages div")
    MESSAGE_PRICE = (By.CSS_SELECTOR, "#messages div p")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

class HeaderPageLocators():
    LOGIN_LINK = (By.ID, "login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".page_inner a.btn-default")
    MAIN_LINK = (By.CSS_SELECTOR, ".page_inner .row .h1 a")

    USER_ICON = (By.CLASS_NAME, "icon-user")

class BasketPageLocators():
    MESSAGE_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
    PRODUCT = (By.CLASS_NAME, "basket-items")

class MainPageLocators():
    SUCCESS_REGISTER_MESSAGE = (By.CLASS_NAME, "alert-success")