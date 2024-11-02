from selenium.webdriver.common.by import By
from features.pages.BasePage import BasePage

class MainPage(BasePage):

    # Constants
    logout_button_xpath = (By.XPATH, "//button[@id='toggleButton' and text()='Logout']")

    # Constructor
    def __init__(self, driver):
        super().__init__(driver)