from selenium.common import NoSuchElementException
from features.pages.BasePage import BasePage


class MainPage(BasePage):

    # Constructor
    def __init__(self, driver):
        super().__init__(driver)


    # Constants
    welcome_header_xpath = "//H2[text()='Welcome to your Vacation Planner']"

    def verify_user_login(self):
        return self.verify_element_exists("welcome_header_xpath", self.welcome_header_xpath)
