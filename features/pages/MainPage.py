from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from features.pages.BasePage import BasePage


class MainPage(BasePage):

    # Constructor
    def __init__(self, driver):
        super().__init__(driver)


    # Constants
    # logout_button_xpath = "//button[@id='toggleButton' and text()='Logout']" # Removed
    plan_vacation_button_xpath = "//input[@type='submit' and @value='Plan Vacation']"

    def verify_user_login(self):
        try:
            element = self.find_element("plan_vacation_button_xpath", self.plan_vacation_button_xpath)
            return element.is_displayed() if element else False
        except NoSuchElementException:
            return False
