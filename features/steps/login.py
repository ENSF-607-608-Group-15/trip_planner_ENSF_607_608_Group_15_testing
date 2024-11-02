from behave import *
from features.pages.LoginPage import LoginPage
from features.pages.MainPage import MainPage


@given(u'I got navigated to Login page')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    assert context.LoginPage.check_login_page_text_exists("Please login!")

@when(u'I click Login button')
def step_impl(context):
    context.main_page = context.login_page.click_on_login_button()

@then(u'I should get an error message with text as {actual_text}"')
def step_impl(context, actual_text):
    assert context.LoginPage.check_login_page_text_exists(actual_text)

@when(u'I enter password as "{password}"')
def step_impl(context, password):
    context.login_page.enter_password(password)

@then(u'I should get logged in')
def step_impl(context):
    pass # TODO: Finish implementation
