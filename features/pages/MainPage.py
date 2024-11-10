from selenium.common import NoSuchElementException
from features.pages.BasePage import BasePage
from utilities.HelperFunctions import format_date_by_locale


class MainPage(BasePage):

    # Constructor
    def __init__(self, driver):
        super().__init__(driver)


    # Constants
    generate_trip_button_xpath = "//*[@class='btn btn-primary']"
    departure_city_textbox_id = "inputCity"
    departure_date_picker_id = "dDate"

    def verify_user_login(self):
        return self.verify_element_exists("generate_trip_button_xpath",
                                          self.generate_trip_button_xpath)

    def enter_departure_date(self, departure_date):
        formatted_date = format_date_by_locale(self.driver, departure_date)
        self.send_keys_into_element("departure_date_picker_id", self.departure_date_picker_id, formatted_date)



