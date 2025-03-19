from .locators import BasketPageLocators
from .base_page import BasePage
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    def should_not_be_goods(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "There are goods in basket"

    def is_basket_empty_message(self):
        basket_is_empty_message = self.browser.find_element(*BasketPageLocators.CONTINUE_SHOPPING).text
        assert basket_is_empty_message == "Continue shopping", "Basket is not empty"