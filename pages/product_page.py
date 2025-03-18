from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()
        self.solve_quiz_and_get_code()
        book_name = self.book_name()
        book_in_basket_name = self.book_in_basket_name()
        book_price = self.book_price()
        book_in_basket_price = self.book_in_basket_price()
        
        assert book_name == book_in_basket_name, "The other book in basket"
        assert book_price == book_in_basket_price, "The price from the other book"

    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), "Add_To_Cart button is not present"

    def book_name(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
    
    def book_in_basket_name(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_BASKET).text

    def book_price(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
    
    def book_in_basket_price(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_PRICE_IN_BASKET).text
