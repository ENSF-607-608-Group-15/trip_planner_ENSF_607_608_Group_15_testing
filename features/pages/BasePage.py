from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoAlertPresentException


class BasePage:
    """
    BasePage serves as a parent class for all page objects.
    It provides common methods for interacting with web elements.
    """

    # Constructor
    def __init__(self, driver):
        """
        Initializes the BasePage with a WebDriver instance.

        :param driver: WebDriver instance used to interact with the web page.
        """
        self.driver = driver


    # Methods
    def find_element(self, locator_type, locator_value, wait_time=15):
        """
        Finds a web element based on the locator type and value.

        :param locator_type: The type of locator (e.g., '_id', '_name', '_xpath').
        :param locator_value: The value of the locator.
        :param wait_time: Maximum time to wait for the element to be visible.
        :return: The web element if found.
        """
        element = None
        if locator_type.endswith("_id"):
            element = WebDriverWait(self.driver, wait_time).until(
                EC.visibility_of_element_located((By.ID, locator_value))
            )
        elif locator_type.endswith("_name"):
            element = WebDriverWait(self.driver, wait_time).until(
                EC.visibility_of_element_located((By.NAME, locator_value))
            )
        elif locator_type.endswith("_class_name"):
            element = WebDriverWait(self.driver, wait_time).until(
                EC.visibility_of_element_located((By.CLASS_NAME, locator_value))
            )
        elif locator_type.endswith("_link_text"):
            element = WebDriverWait(self.driver, wait_time).until(
                EC.visibility_of_element_located((By.LINK_TEXT, locator_value))
            )
        elif locator_type.endswith("_xpath"):
            element = WebDriverWait(self.driver, wait_time).until(
                EC.visibility_of_element_located((By.XPATH, locator_value))
            )
        elif locator_type.endswith("_css"):
            element = WebDriverWait(self.driver, wait_time).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, locator_value))
            )

        if element:
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()

        return element


    def click_on_element(self, locator_type, locator_value):
        """
        Clicks on a web element specified by the locator type and value.

        :param locator_type: The type of locator (e.g., '_id', '_name', '_xpath').
        :param locator_value: The value of the locator.
        """
        element = self.find_element(locator_type, locator_value)
        element.click()


    def verify_page_title(self, expected_title_text):
        """
        Verifies that the current page title matches the expected title.

        :param expected_title_text: The expected title text of the page.
        :return: True if the title matches, False otherwise.
        """
        self.driver.title.__eq__(expected_title_text)


    def verify_element_exists(self, locator_type, locator_value):
        """
        Verifies if an element exists and is displayed on the page.

        :param locator_type: The type of locator (e.g., '_id', '_name', '_xpath').
        :param locator_value: The value of the locator.
        :return: True if the element is displayed, False otherwise.
        """
        try:
            element = self.find_element(locator_type, locator_value)
            return element.is_displayed() if element else False
        except NoSuchElementException:
            return False


    def send_keys_into_element(self, locator_type, locator_value, text):
        """
        Sends text input to a web element specified by the locator type and value.

        :param locator_type: The type of locator (e.g., '_id', '_name', '_xpath').
        :param locator_value: The value of the locator.
        :param text: The text to send to the element.
        """
        element = self.find_element(locator_type, locator_value)
        element.click()
        element.clear()
        element.send_keys(text)


    def element_text_contains(self, locator_type, locator_value, expected_text):
        """
        Checks if the text of a web element contains the expected text.

        :param locator_type: The type of locator (e.g., '_id', '_name', '_xpath').
        :param locator_value: The value of the locator.
        :param expected_text: The text expected to be contained in the element.
        :return: True if the element's text contains the expected text, False otherwise.
        """
        element = self.find_element(locator_type, locator_value)
        return expected_text in element.text and element.is_displayed()


    def element_text_equals(self, locator_type, locator_value, expected_text):
        """
        Checks if the text of a web element equals the expected text.

        :param locator_type: The type of locator (e.g., '_id', '_name', '_xpath').
        :param locator_value: The value of the locator.
        :param expected_text: The text expected to match the element's text.
        :return: True if the element's text equals the expected text, False otherwise.
        """
        element = self.find_element(locator_type, locator_value)
        return element.text == expected_text and element.is_displayed()


    def verify_validation_message(self, locator_type, locator_value, expected_message):
        """
        Verifies that the validation message of an element matches the expected message.

        :param locator_type: The type of locator (e.g., '_id', '_name', '_xpath').
        :param locator_value: The value of the locator.
        :param expected_message: The expected validation message.
        :return: True if the validation message matches, False otherwise.
        """
        element = self.find_element(locator_type, locator_value)
        actual_message = element.get_attribute("validationMessage")
        return (expected_message == actual_message) and element.is_displayed()


    def is_alert_present(self):
        """
        Checks if an alert is present on the page.

        :return: The alert object if present, None otherwise.
        """
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            return alert
        except NoAlertPresentException:
            return None

    def verify_alert_message_equals(self, expected_message):
        """
        Verifies that the alert message equals the expected message.

        :param expected_message: The expected alert message.
        :return: True if the alert message matches, False otherwise.
        """
        alert = self.is_alert_present()
        if alert:
            actual_message = alert.text
            alert.accept()
            return actual_message == expected_message
        return False

    def verify_text_contains_list(self, locator_type, locator_value, list_of_words, expected=True):
        """
        Verifies that the text of an element contains or does not contain a list of words.

        :param locator_type: The type of locator (e.g., '_id', '_name', '_xpath').
        :param locator_value: The value of the locator.
        :param list_of_words: List of words to check in the element's text.
        :param expected: Boolean indicating if the words are expected to be present (True) or absent (False).
        :return: True if the condition is met for all words, False otherwise.
        """
        for word in list_of_words:
            element_contains_word = self.element_text_contains(locator_type, locator_value, word)
            if expected and not element_contains_word:
                print(f"Expected word '{word}' was not found in element text.")
                return False
            elif not expected and element_contains_word:
                print(f"Unexpected word '{word}' was found in element text.")
                return False
        return True
