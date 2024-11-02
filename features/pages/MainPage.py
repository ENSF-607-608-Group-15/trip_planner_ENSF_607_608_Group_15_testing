from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from features.pages.BasePage import BasePage


class MainPage(BasePage):

    # Constructor
    def __init__(self, driver):
        super().__init__(driver)


    # Constants
    logout_button_xpath = "//button[@id='toggleButton' and text()='Logout']"

    def verify_user_login(self):
        try:
            element = self.find_element("logout_button_xpath", self.logout_button_xpath)
            return element.is_displayed() if element else False
        except NoSuchElementException:
            return False
