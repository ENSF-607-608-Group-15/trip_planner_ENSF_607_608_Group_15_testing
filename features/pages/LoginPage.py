from features.pages.BasePage import BasePage
from features.pages.MainPage import MainPage


class LoginPage(BasePage):

    # Constructor
    def __init__(self, driver):
        super().__init__(driver)

    # Constants
    login_button_id = "loginbtn"
    guest_button_id = "guestbtn"
    username_login_textbox_name = "usernameLogin"
    password_login_textbox_name = "passwordLogin"
    signup_label_xpath = "//label[text()='Sign up']"
    error_message_xpath = "//*[@class='login']//*[@id='errorMessage']"

    # Methods
    def enter_username(self, username_text):
        self.send_keys_into_element("username_login_textbox_name", self.username_login_textbox_name,
                                    username_text)

    def enter_password(self, password_text):
        self.send_keys_into_element(
            "password_login_textbox_name", self.password_login_textbox_name, password_text)

    def click_on_login_button(self):
        self.click_on_element("login_button_id", self.login_button_id)
        return MainPage(self.driver)

    def verify_username_validation_message(self, expected_message):
        return self.verify_validation_message("username_login_textbox_name", self.username_login_textbox_name, expected_message)

    def verify_page_is_active(self):
        element_exists = self.verify_element_exists("login_button_id", self.login_button_id)
        return element_exists

    def click_on_signup_view(self):
        self.click_on_element("signup_label_xpath", self.signup_label_xpath)

    def verify_error_message_equals(self, expected_message):
        return self.element_text_equals("error_message_xpath", self.error_message_xpath, expected_message)

    def click_on_guest_button(self):
        self.click_on_element("guest_button_id", self.guest_button_id)
        return MainPage(self.driver)
