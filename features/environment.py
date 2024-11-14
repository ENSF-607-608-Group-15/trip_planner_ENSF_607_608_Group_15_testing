import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from utilities import ConfigReader


def before_scenario(context, driver):
    """
    Sets up the browser environment before each test scenario.

    :param context: Behave context object that holds the state for the test.
    :param driver: WebDriver instance used to interact with the browser.
    """
    browser_name = ConfigReader.read_config("basic info", "browser")
    if browser_name.__eq__("chrome"):
        context.driver = webdriver.Chrome()
    elif browser_name.__eq__("firefox"):
        context.driver = webdriver.Firefox()
    elif browser_name.__eq__("edge"):
        context.driver = webdriver.Edge()
    elif browser_name.__eq__("safari"):
        context.driver = webdriver.Safari()

    context.driver.maximize_window()
    context.driver.get(ConfigReader.read_config("basic info", "url"))


def after_scenario(context, driver):
    """
    Cleans up the browser environment after each test scenario.

    :param context: Behave context object that holds the state for the test.
    :param driver: WebDriver instance used to interact with the browser.
    """
    context.driver.quit()


def after_step(context, step):
    """
    Takes a screenshot if a test step fails.

    :param context: Behave context object that holds the state for the test.
    :param step: The current step in the test scenario.
    """
    if step.status == "failed":
        allure.attach(context.driver.get_screenshot_as_png(),
                      name="failed_screenshot",
                      attachment_type=AttachmentType.PNG)
