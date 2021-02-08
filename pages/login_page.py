from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators
import time


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        assert 'login' in self.browser.current_url, "url hasn't 'login'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_MAIL), "Login mail is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login password is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_MAIL), "Register mail is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD1), "Register password1 is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD2), "Register password2 is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), "Register button is not presented"
        
    def register_new_user(self, email, password):
        mail_place = self.browser.find_element(*LoginPageLocators.REGISTER_MAIL)
        mail_place.send_keys(email)
        password1_place = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1)
        password1_place.send_keys(password)
        password2_place = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2)
        password2_place.send_keys(password)       
        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()
        
        