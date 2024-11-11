from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoAlertPresentException


class BasePage:


    # Constructor
    def __init__(self, driver):
        self.driver = driver


    # Methods
    def find_element(self, locator_type, locator_value, wait_time=30):
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
        element = self.find_element(locator_type, locator_value)
        element.click()


    def verify_page_title(self, expected_title_text):
        self.driver.title.__eq__(expected_title_text)


    def verify_element_exists(self, locator_type, locator_value):
        try:
            element = self.find_element(locator_type, locator_value)
            return element.is_displayed() if element else False
        except NoSuchElementException:
            return False


    def send_keys_into_element(self, locator_type, locator_value, text):
        element = self.find_element(locator_type, locator_value)
        element.click()
        element.clear()
        element.send_keys(text)


    def element_text_contains(self, locator_type, locator_value, expected_text):
        element = self.find_element(locator_type, locator_value)
        return expected_text in element.text and element.is_displayed()


    def element_text_equals(self, locator_type, locator_value, expected_text):
        element = self.find_element(locator_type, locator_value)
        return element.text == expected_text and element.is_displayed()


    def verify_validation_message(self, locator_type, locator_value, expected_message):
        element = self.find_element(locator_type, locator_value)
        actual_message = element.get_attribute("validationMessage")
        return (expected_message == actual_message) and element.is_displayed()


    def is_alert_present(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            return alert
        except NoAlertPresentException:
            return None

    def verify_alert_message_equals(self, expected_message):
        alert = self.is_alert_present()
        if alert:
            actual_message = alert.text
            alert.accept()
            return actual_message == expected_message
        return False

    def verify_text_contains_list(self, locator_type, locator_value, list_of_words, expected=True):
        for word in list_of_words:
            element_contains_word = self.element_text_contains(locator_type, locator_value, word)
            if expected and not element_contains_word:
                print(f"Expected word '{word}' was not found in element text.")
                return False
            elif not expected and element_contains_word:
                print(f"Unexpected word '{word}' was found in element text.")
                return False
        return True
