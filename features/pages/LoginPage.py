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


    # Methods
    def enter_username(self, username_text):
        self.send_keys_into_element("username_login_textbox_name", self.username_login_textbox_name, username_text)
        

    def enter_password(self, password_text):
        self.send_keys_into_element("password_login_textbox_name", self.password_login_textbox_name, password_text)


    def click_on_login_button(self):
        self.click_on_element("login_button_id", self.login_button_id)
        return MainPage(self.driver)
