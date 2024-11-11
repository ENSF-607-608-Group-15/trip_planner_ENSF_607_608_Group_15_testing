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
    desired_location_textbox_id = "tripLocation"
    return_date_picker_id = "rDate"
    budget_textbox_id = "tripBudget"
    no_flying_checkbox_id = "noFlying"
    disability_friendly_checkbox_id = "disabilityFriendly"
    family_friendly_checkbox_id = "familyFriendly"
    group_discount_checkbox_id = "groupDiscount"
    trip_theme_textbox_id = "tripTheme"
    previous_setting_button_id = "prvsettings"
    previous_vacation_plan_button_id = "prvResponses"
    logout_button_id = "logoutbtn"
    plan_content_xpath = "//*[@class='plan-content']"
    previous_plan_xpath = "//*[@class='vacation']"
    error_message_xpath = "//*[@class='form-control']//*[@id='errorMessage']"

    # Methods
    def verify_user_login(self):
        return self.verify_element_exists("generate_trip_button_xpath", self.generate_trip_button_xpath)


    def enter_departure_date(self, departure_date):
        formatted_date = format_date_by_locale(self.driver, departure_date)
        self.send_keys_into_element("departure_date_picker_id", self.departure_date_picker_id, formatted_date)


    def enter_departure_city(self, departure_city_text):
        self.send_keys_into_element("departure_city_textbox_id", self.departure_city_textbox_id, departure_city_text)


    def enter_desired_location(self, desired_location_text):
        self.send_keys_into_element("desired_location_textbox_id", self.desired_location_textbox_id, desired_location_text)


    def enter_return_date(self, return_date):
        formatted_date = format_date_by_locale(self.driver, return_date)
        self.send_keys_into_element("return_date_picker_id", self.return_date_picker_id, formatted_date)


    def enter_budget(self, budget):
        self.send_keys_into_element("budget_textbox_id", self.budget_textbox_id, budget)


    def enter_theme(self, theme):
        self.send_keys_into_element("trip_theme_textbox_id", self.trip_theme_textbox_id, theme)


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


    def click_on_family_friendly_checkbox(self):
        self.click_on_element("family_friendly_checkbox_id", self.family_friendly_checkbox_id)


    def click_on_no_flying_checkbox(self):
        self.click_on_element("no_flying_checkbox_id", self.no_flying_checkbox_id)


    def click_on_disability_friendly_checkbox(self):
        self.click_on_element("disability_friendly_checkbox_id", self.disability_friendly_checkbox_id)


    def click_on_group_discount_checkbox(self):
        self.click_on_element("group_discount_checkbox_id", self.group_discount_checkbox_id)


    def verify_suggestions_text_contain(self, keywords_list):
        return self.verify_text_contains_list("plan_content_xpath", self.plan_content_xpath, keywords_list)


    def verify_suggestions_text_not_contain(self, keywords_list):
        return self.verify_text_contains_list("plan_content_xpath", self.plan_content_xpath, keywords_list, expected=False)


    def verify_error_popup(self, expected_message):
        return self.verify_alert_message_equals(expected_message)


    def verify_return_date_error_message(self, expected_message):
        return self.verify_validation_message("return_date_picker_id", self.return_date_picker_id, expected_message)


    def verify_error_message_equals(self, expected_message):
        return self.element_text_equals("error_message_xpath", self.error_message_xpath, expected_message)
