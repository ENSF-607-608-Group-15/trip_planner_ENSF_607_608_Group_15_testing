from behave import *
from features.pages.LoginPage import LoginPage
from features.pages.SignupPage import SignupPage
from utilities.HelperFunctions import generate_random_string


@when(u'I click Sign up button')
def step_impl(context):
    context.login_page.click_on_signup_button()


@then(u'I should be navigated to the Sign up page')
def step_impl(context):
    context.signup_page = SignupPage(context.driver)
    assert context.signup_page.verify_page_is_active()


@when(u'I enter username as random_username')
def step_impl(context):
    context.username = generate_random_string(7)
    context.signup_page.enter_username(context.username)


@when(u'I enter password as random_password')
def step_impl(context):
    context.password = generate_random_string(12)
    context.signup_page.enter_password(context.password)

@when(u'I click sign up botton')
def step_impl(context):
    context.signup_page.click_on_signup_button()

@then(u'I should get an error message with text as "{expected_text}"')
def step_impl(context, expected_text):
    assert context.signup_page.check_username_error_message(expected_text)

@then(u'I should be navigated to the Login page')
def step_impl(context):
    context.login_page = context.signup_page.switch_to_login_view()
    assert context.login_page.verify_page_is_active()

@when(u'I enter username as "{username}"')
def step_impl(context, username):
    context.signup_page.enter_username(username)

@when(u'I enter password as "{password}"')
def step_impl(context, password):
    context.signup_page.enter_password(password)

@then(u'I should get a username error message with text as "{expected_text}"')
def step_impl(context, expected_text):
   assert context.signup_page.check_username_error_message(expected_text)

@then(u'I should get a password error message with text as "{expected_text}"')
def step_impl(context, expected_text):
   assert context.signup_page.check_password_error_message(expected_text)

@then(u'I should see confirm message with text as "{expected_text}"')
def step_impl(context):
    pass