from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):

    def add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_LINK), "Basket link is not presented"
        basket_link = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
        basket_link.click()
        self.solve_quiz_and_get_code()

    def should_be_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        book_name_in_basket = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_BASKET).text
        assert book_name == book_name_in_basket, "In basket is wrong book"
        
    def should_be_book_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        book_price_in_basket = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_IN_BASKET).text
        assert book_price == book_price_in_basket, "In basket is wrong price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
       
    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
