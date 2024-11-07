from features.pages.BasePage import BasePage
from features.pages.MainPage import MainPage

class LoginPage(BasePage):

    # Constructor
    def __init__(self, driver):
        super().__init__(driver)


    # Constants
    login_button_id = "loginbtn"
    username_login_textbox_name = "usernameLogin"
    password_login_textbox_name = "passwordLogin"
    signup_button_xpath = "/html/body/div[1]/div[1]/form[3]/label"

    # Methods
    def enter_username(self, username_text):
        self.send_keys_into_element("username_login_textbox_name", self.username_login_textbox_name,
                                    username_text)
        

    def enter_password(self, password_text):
        self.send_keys_into_element("password_login_textbox_name",self.password_login_textbox_name, password_text)


    def click_on_login_button(self):
        self.click_on_element("login_button_id", self.login_button_id)
        return MainPage(self.driver)

    def check_username_error_message(self, expected_message):
        return self.verify_validation_message("username_login_textbox_name", self.username_login_textbox_name, expected_message)

    def check_page_is_active(self):
        element_exists = self.verify_element_exists("login_button_id", self.login_button_id)
        return element_exists
    
    def click_on_signup_button(self):
        self.click_on_element("signup_button_xpath", self.signup_button_xpath)