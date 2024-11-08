from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:


    # Constructor
    def __init__(self, driver):
        self.driver = driver


    # Methods
    def find_element(self, locator_type, locator_value, wait_time=10):
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
        return element.text.__contains__(expected_text) and element.is_displayed()


    def element_text_equals(self, locator_type, locator_value, expected_text):
        element = self.find_element(locator_type, locator_value)
        return element.text == expected_text and element.is_displayed()

    def verify_validation_message(self, locator_type, locator_value, expected_message):
        element = self.find_element(locator_type, locator_value)
        actual_message = element.get_attribute("validationMessage")
        return (expected_message == actual_message) and element.is_displayed()
