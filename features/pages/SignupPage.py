from features.pages.BasePage import BasePage


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
    error_message_xpath = "//*[@class='signup']//*[@id='errorMessage']"

    # Methods
    def enter_password(self, password_text):
        self.send_keys_into_element("password_signup_textbox_name", self.password_signup_textbox_name, password_text)


    def enter_username(self, username_text):
        self.send_keys_into_element(
            "username_signup_textbox_name", self.username_signup_textbox_name, username_text)
        

    def click_on_login_view(self):
        self.click_on_element("login_label_xpath", self.login_label_xpath)
    

    def verify_page_is_active(self):
        element_exists = self.verify_element_exists("signup_button_id", self.signup_button_id)
        return element_exists
    

    def click_on_signup_button(self):
        self.click_on_element("signup_button_id", self.signup_button_id)
    

    def verify_username_error_message(self, expected_message):
        return self.verify_validation_message("username_signup_textbox_name", self.username_signup_textbox_name, expected_message)


    def verify_password_error_message(self, expected_message):
        return self.verify_validation_message("password_signup_textbox_name", self.password_signup_textbox_name, expected_message)


    def verify_error_message_equals(self, expected_message):
        return self.element_text_equals("error_message_xpath", self.error_message_xpath, expected_message)

    