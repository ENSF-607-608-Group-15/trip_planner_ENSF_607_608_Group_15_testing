from features.pages.BasePage import BasePage
from features.pages.LoginPage import LoginPage
import string
import random

class SignupPage(BasePage):

    # Constructor
    def __init__(self, driver):
        super().__init__(driver)


    # Constants
    login_label_xpath = "//label[text()='Login']"
    username_signup_textbox_name = "usernameSignUp"
    password_signup_textbox_name = "passwordSignUp"
    signup_button_id = "signupbtn"
    guest_id = "guestbtn"
    signup_error_message = "errorMessage"

    # Methods
    def enter_password(self, password_text):
        self.send_keys_into_element("password_signup_textbox_name", self.password_signup_textbox_name, password_text)


    def enter_username(self, username_text):
        self.send_keys_into_element("username_signup_textbox_name", self.username_signup_textbox_name, username_text)


    def switch_to_login_view(self):
        self.click_on_element("login_label_xpath", self.login_label_xpath)
        return LoginPage(self.driver)


    def check_page_is_active(self):
        element_exists = self.verify_element_exists("signup_button_id", self.signup_button_id)
        return element_exists

    def click_on_signup_button(self):
        self.click_on_element("signup_button_id", self.signup_button_id)
        return SignupPage(self.driver)
    
    def random_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
    
    def check_username_error_message(self, expected_message):
        return self.verify_validation_message("username_signup_textbox_name", self.username_signup_textbox_name, expected_message)
    
    def check_password_error_message(self, expected_message):
        return self.verify_validation_message("password_signup_textbox_name ", self.password_signup_textbox_name, expected_message)