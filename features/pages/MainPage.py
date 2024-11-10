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
    # departure_city_textbox_name = "inputCity"
    desired_location_textbox_name  = "tripLocation"
    # departure_date_id = "dDate"
    return_date_id = "rDate"
    budget_textbox_id = "tripBudget"
    no_flying_checkbox_id = "noFlying"
    disability_friendly_checkbox_id = "disabilityFriendly"
    family_friendly_checkbox_id = "familyFriendly"
    group_discount_checkbox_id = "groupDiscount"
    trip_theme_textbox_id = "tripTheme"
    previous_setting_button_id = "prvsettings"
    previous_vacation_plan_button_id = "prvResponses"
    logout_button_id = "logoutbtn"
    plan_content_xpath = "//div[contains(@class, 'plan-content')]" 
    previous_plan_xpath = "//div[contains(@class, 'vacation')]"

    def verify_user_login(self):
        return self.verify_element_exists("generate_trip_button_xpath",
                                          self.generate_trip_button_xpath)

    def enter_departure_date(self, departure_date):
        formatted_date = format_date_by_locale(self.driver, departure_date)
        self.send_keys_into_element("departure_date_picker_id", self.departure_date_picker_id, formatted_date)



    def enter_departure_city(self, departure_city_text):
        self.send_keys_into_element("departure_city_textbox_name", self.departure_city_textbox_name, departure_city_text)

    def enter_desired_location(self, desired_location_text):
        self.send_keys_into_element("desired_location_textbox_name", self.desired_location_textbox_name, desired_location_text)
    
    # def enter_departure_date(self, departure_date_text):
    #     self.send_keys_into_element("departure_date_id", self.departure_date_id, departure_date_text)

    def enter_return_date(self, return_date_text):
        self.send_keys_into_element("return_date_id", self.return_date_id, return_date_text)

    def click_on_generate_trip_button(self):
        self.click_on_element("generate_trip_button_xpath", self.generate_trip_button_xpath)    

    def verify_plan_content_is_active(self):
        element_exists = self.verify_element_exists("plan_content_xpath", self.plan_content_xpath)
        return element_exists
    
    def click_on_previous_plan_button(self):
        self.click_on_element("previous_vacation_plan_button_id", self.previous_vacation_plan_button_id)
    
    def verify_previous_plan_is_active(self):
        element_exists = self.verify_element_exists("previous_plan_xpath", self.previous_plan_xpath)
        return element_exists
