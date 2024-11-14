from features.pages.BasePage import BasePage


class SignupPage(BasePage):
    """
    SignupPage represents the signup page of the application.
    It extends BasePage and includes methods specific to the signup page.
    """

    # Constructor
    def __init__(self, driver):
        """
        Initializes the SignupPage with a WebDriver instance.

        :param driver: WebDriver instance used to interact with the signup page.
        """
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
        """
        Enters the password into the signup password textbox.

        :param password_text: The password to be entered.
        """
        self.send_keys_into_element("password_signup_textbox_name", self.password_signup_textbox_name, password_text)


    def enter_username(self, username_text):
        """
        Enters the username into the signup username textbox.

        :param username_text: The username to be entered.
        """
        self.send_keys_into_element(
            "username_signup_textbox_name", self.username_signup_textbox_name, username_text)
        

    def click_on_login_view(self):
        """
        Clicks the login label to navigate to the login view.
        """
        self.click_on_element("login_label_xpath", self.login_label_xpath)
    

    def verify_page_is_active(self):
        """
        Verifies that the signup page is active by checking the presence of the signup button.

        :return: True if the signup button is present, False otherwise.
        """
        element_exists = self.verify_element_exists("signup_button_id", self.signup_button_id)
        return element_exists
    

    def click_on_signup_button(self):
        """
        Clicks the signup button to submit the signup form.
        """
        self.click_on_element("signup_button_id", self.signup_button_id)
    

    def verify_username_error_message(self, expected_message):
        """
        Verifies that the username error message matches the expected message.

        :param expected_message: The expected error message text.
        :return: True if the error message matches, False otherwise.
        """
        return self.verify_validation_message("username_signup_textbox_name", self.username_signup_textbox_name, expected_message)


    def verify_password_error_message(self, expected_message):
        """
        Verifies that the password error message matches the expected message.

        :param expected_message: The expected error message text.
        :return: True if the error message matches, False otherwise.
        """
        return self.verify_validation_message("password_signup_textbox_name", self.password_signup_textbox_name, expected_message)


    def verify_error_message_equals(self, expected_message):
        """
        Verifies that the error message displayed on the signup page matches the expected message.

        :param expected_message: The expected error message text.
        :return: True if the error message matches, False otherwise.
        """
        return self.element_text_equals("error_message_xpath", self.error_message_xpath, expected_message)
    