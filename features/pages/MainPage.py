from selenium.common import NoSuchElementException
from features.pages.BasePage import BasePage
from utilities.HelperFunctions import format_date_by_locale


class MainPage(BasePage):
    """
    MainPage represents the main page of the application.
    It extends BasePage and includes methods specific to the main page.
    """

    # Constructor
    def __init__(self, driver):
        """
        Initializes the MainPage with a WebDriver instance.

        :param driver: WebDriver instance used to interact with the main page.
        """
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
    trip_error_message_xpath = "//*[@class='error-message']"
    pdf_download_link_id = "dwnloadpdf"
    trip_previous_settings_xpath = "//*[@class='trip']"

    # Methods
    def verify_user_login(self):
        """
        Verifies that the user is logged in by checking the presence of the generate trip button.

        :return: True if the generate trip button is present, False otherwise.
        """
        return self.verify_element_exists("generate_trip_button_xpath", self.generate_trip_button_xpath)


    def enter_departure_date(self, departure_date):
        """
        Enters the departure date into the date picker.

        :param departure_date: The departure date to be entered.
        """
        formatted_date = format_date_by_locale(self.driver, departure_date)
        self.send_keys_into_element("departure_date_picker_id", self.departure_date_picker_id, formatted_date)


    def enter_departure_city(self, departure_city_text):
        """
        Enters the departure city into the city textbox.

        :param departure_city_text: The departure city to be entered.
        """
        self.send_keys_into_element("departure_city_textbox_id", self.departure_city_textbox_id, departure_city_text)


    def enter_desired_location(self, desired_location_text):
        """
        Enters the desired location into the location textbox.

        :param desired_location_text: The desired location to be entered.
        """
        self.send_keys_into_element("desired_location_textbox_id", self.desired_location_textbox_id, desired_location_text)


    def enter_return_date(self, return_date):
        """
        Enters the return date into the date picker.

        :param return_date: The return date to be entered.
        """
        formatted_date = format_date_by_locale(self.driver, return_date)
        self.send_keys_into_element("return_date_picker_id", self.return_date_picker_id, formatted_date)


    def enter_budget(self, budget):
        """
        Enters the budget into the budget textbox.

        :param budget: The budget to be entered.
        """
        self.send_keys_into_element("budget_textbox_id", self.budget_textbox_id, budget)


    def enter_theme(self, theme):
        """
        Enters the trip theme into the theme textbox.

        :param theme: The trip theme to be entered.
        """
        self.send_keys_into_element("trip_theme_textbox_id", self.trip_theme_textbox_id, theme)


    def click_on_generate_trip_button(self):
        """
        Clicks the generate trip button to create a trip plan.
        """
        self.click_on_element("generate_trip_button_xpath", self.generate_trip_button_xpath)


    def verify_plan_content_is_active(self):
        """
        Verifies that the plan content is active by checking its presence.

        :return: True if the plan content is present, False otherwise.
        """
        element_exists = self.verify_element_exists("plan_content_xpath", self.plan_content_xpath)
        return element_exists


    def click_on_previous_plan_button(self):
        """
        Clicks the button to view previous vacation plans.
        """
        self.click_on_element("previous_vacation_plan_button_id", self.previous_vacation_plan_button_id)


    def verify_previous_plan_is_active(self):
        """
        Verifies that the previous plan is active by checking its presence.

        :return: True if the previous plan is present, False otherwise.
        """
        element_exists = self.verify_element_exists("previous_plan_xpath", self.previous_plan_xpath)
        return element_exists


    def click_on_family_friendly_checkbox(self):
        """
        Clicks the family-friendly checkbox to select the option.
        """
        self.click_on_element("family_friendly_checkbox_id", self.family_friendly_checkbox_id)


    def click_on_no_flying_checkbox(self):
        """
        Clicks the no-flying checkbox to select the option.
        """
        self.click_on_element("no_flying_checkbox_id", self.no_flying_checkbox_id)


    def click_on_disability_friendly_checkbox(self):
        """
        Clicks the disability-friendly checkbox to select the option.
        """
        self.click_on_element("disability_friendly_checkbox_id", self.disability_friendly_checkbox_id)


    def click_on_group_discount_checkbox(self):
        """
        Clicks the group discount checkbox to select the option.
        """
        self.click_on_element("group_discount_checkbox_id", self.group_discount_checkbox_id)


    def verify_suggestions_text_contain(self, keywords_list):
        """
        Verifies that the suggestions text contains all specified keywords.

        :param keywords_list: List of keywords to check in the suggestions text.
        :return: True if all keywords are found, False otherwise.
        """
        return self.verify_text_contains_list("plan_content_xpath", self.plan_content_xpath, keywords_list)


    def verify_suggestions_text_not_contain(self, keywords_list):
        """
        Verifies that the suggestions text does not contain any of the specified keywords.

        :param keywords_list: List of keywords to check in the suggestions text.
        :return: True if none of the keywords are found, False otherwise.
        """
        return self.verify_text_contains_list("plan_content_xpath", self.plan_content_xpath, keywords_list, expected=False)


    def verify_error_popup(self, expected_message):
        """
        Verifies that an error popup message matches the expected message.

        :param expected_message: The expected error message text.
        :return: True if the error message matches, False otherwise.
        """
        return self.verify_alert_message_equals(expected_message)


    def verify_return_date_error_message(self, expected_message):
        """
        Verifies that the return date error message matches the expected message.

        :param expected_message: The expected error message text.
        :return: True if the error message matches, False otherwise.
        """
        return self.verify_validation_message("return_date_picker_id", self.return_date_picker_id, expected_message)


    def verify_error_message_equals(self, expected_message):
        """
        Verifies that the error message displayed on the page matches the expected message.

        :param expected_message: The expected error message text.
        :return: True if the error message matches, False otherwise.
        """
        return self.element_text_equals("error_message_xpath", self.error_message_xpath, expected_message)


    def verify_pdf_download_link_exists(self):
        """
        Verifies that the PDF download link exists on the page.

        :return: True if the PDF download link is present, False otherwise.
        """
        return self.verify_element_exists("pdf_download_link_id", self.pdf_download_link_id)


    def verify_trip_error_message_contains(self, keywords_list):
        """
        Verifies that the trip error message contains all specified keywords.

        :param keywords_list: List of keywords to check in the trip error message.
        :return: True if all keywords are found, False otherwise.
        """
        return self.verify_text_contains_list("trip_error_message_xpath", self.trip_error_message_xpath, keywords_list)


    def verify_trip_previous_settings_contains(self, keywords_list):
        """
        Verifies that the trip previous settings contain all specified keywords.

        :param keywords_list: List of keywords to check in the trip previous settings.
        :return: True if all keywords are found, False otherwise.
        """
        return self.verify_text_contains_list("trip_previous_settings_xpath", self.trip_previous_settings_xpath, keywords_list)


    def click_on_previous_settings_button(self):
        """
        Clicks the button to view previous trip settings.
        """
        self.click_on_element("previous_setting_button_id", self.previous_setting_button_id)
