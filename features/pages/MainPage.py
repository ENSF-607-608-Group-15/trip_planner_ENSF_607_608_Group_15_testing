from selenium.common import NoSuchElementException
from features.pages.BasePage import BasePage


class MainPage(BasePage):

    # Constructor
    def __init__(self, driver):
        super().__init__(driver)


    # Constants
    generate_trip_button_xpath = "//*[@class='btn btn-primary']"

    def verify_user_login(self):
        return self.verify_element_exists("generate_trip_button_xpath",
                                          self.generate_trip_button_xpath)
