from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = "login"
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CLASS_NAME, "btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".col-sm-6 h1")
    BOOK_NAME_IN_BASKET = (By.CSS_SELECTOR, "#messages :nth-child(2) strong")
    BOOK_PRICE = (By.CSS_SELECTOR, ".col-sm-6 .price_color")
    BOOK_PRICE_IN_BASKET = (By.CSS_SELECTOR, "#messages :nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group > a.btn")

class BasketPageLocators():
    BASKET_ITEMS = (By.CLASS_NAME, "basket_items")
    CONTINUE_SHOPPING = (By.CSS_SELECTOR, "#content_inner p a")