from features.pages.BasePage import BasePage
from features.pages.MainPage import MainPage


class LoginPage(BasePage):
    """
    LoginPage represents the login page of the application.
    It extends BasePage and includes methods specific to the login page.
    """

    # Constructor
    def __init__(self, driver):
        """
        Initializes the LoginPage with a WebDriver instance.

        :param driver: WebDriver instance used to interact with the login page.
        """
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
        """
        Enters the username into the login username textbox.

        :param username_text: The username to be entered.
        """
        self.send_keys_into_element("username_login_textbox_name", self.username_login_textbox_name,
                                    username_text)

    def enter_password(self, password_text):
        """
        Enters the password into the login password textbox.

        :param password_text: The password to be entered.
        """
        self.send_keys_into_element(
            "password_login_textbox_name", self.password_login_textbox_name, password_text)

    def click_on_login_button(self):
        """
        Clicks the login button and navigates to the MainPage.

        :return: An instance of MainPage.
        """
        self.click_on_element("login_button_id", self.login_button_id)
        return MainPage(self.driver)

    def verify_username_validation_message(self, expected_message):
        """
        Verifies that the username validation message matches the expected message.

        :param expected_message: The expected validation message text.
        :return: True if the validation message matches, False otherwise.
        """
        return self.verify_validation_message("username_login_textbox_name", self.username_login_textbox_name, expected_message)

    def verify_page_is_active(self):
        """
        Verifies that the login page is active by checking the presence of the login button.

        :return: True if the login button is present, False otherwise.
        """
        element_exists = self.verify_element_exists("login_button_id", self.login_button_id)
        return element_exists

    def click_on_signup_view(self):
        """
        Clicks the signup label to navigate to the signup view.
        """
        self.click_on_element("signup_label_xpath", self.signup_label_xpath)

    def verify_error_message_equals(self, expected_message):
        """
        Verifies that the error message displayed on the login page matches the expected message.

        :param expected_message: The expected error message text.
        :return: True if the error message matches, False otherwise.
        """
        return self.element_text_equals("error_message_xpath", self.error_message_xpath, expected_message)

    def click_on_guest_button(self):
        """
        Clicks the guest button to continue as a guest and navigates to the MainPage.

        :return: An instance of MainPage.
        """
        self.click_on_element("guest_button_id", self.guest_button_id)
        return MainPage(self.driver)
