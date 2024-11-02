from selenium.webdriver.common.by import By

class BasePage:


    # Constructor
    def __init__(self, driver):
        self.driver = driver


    # Methods
    def find_element(self, locator_type, locator_value):
        element = None
        if locator_type.endswith("_id"):
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_type.endswith("_name"):
            element = self.driver.find_element(By.NAME, locator_value)
        elif locator_type.endswith("_class_name"):
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        elif locator_type.endswith("_link_text"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_type.endswith("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)
        elif locator_type.endswith("_css"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        return element


    def click_on_element(self, locator_type, locator_value):
        element = self.find_element(locator_type, locator_value)
        element.click()


    def verify_page_title(self, expected_title_text):
        self.driver.title.__eq__(expected_title_text)


    def verify_text_exists(self, expected_text):
        elements = self.driver.find_elements(By.XPATH, "//*")
        for element in elements:
            if expected_text in element.text:
                return True
        return False


    def send_keys_into_element(self, locator_type, locator_value, text):
        element = self.find_element(locator_type, locator_value)
        element.click()
        element.clear()
        element.send_keys(text)


    def element_text_contains(self, locator_type, locator_value, expected_text):
        element = self.find_element(locator_type, locator_value)
        return element.text.__contains__(expected_text)


    def element_text_equals(self, locator_type, locator_value, expected_text):
        element = self.find_element(locator_type, locator_value)
        return element.text.__eq__(expected_text)
