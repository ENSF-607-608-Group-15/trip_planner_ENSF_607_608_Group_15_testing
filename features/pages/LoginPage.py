from selenium.webdriver.common.by import By
from features.pages.BasePage import BasePage
from features.pages.MainPage import MainPage


class LoginPage(BasePage):

    # Constants
    login_button_xpath = (By.XPATH, "//button[@id='toggleButton' and text()='Login']")
    password_textbox_id = (By.ID, "passwordInput")

    # Constructor
    def __init__(self, driver):
        super().__init__(driver)

    # Methods
    def enter_password(self, password_text):
        self.input_text("password_textbox_id", self.password_textbox_id, password_text)

    def click_on_login_button(self):
        self.click_on_element("login_button_xpath", self.login_button_xpath)
        return MainPage(self.driver)

    def check_login_page_text_exists(self, text):
        return self.verify_text_exists(text)
