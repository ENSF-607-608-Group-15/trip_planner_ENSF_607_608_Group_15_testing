from behave import *
from features.pages.LoginPage import LoginPage
from utilities.HelperFunctions import generate_random_string


@then(u'I should be navigated to the Sign up page')
def step_impl(context):
    assert context.signup_page.verify_page_is_active()


@when(u'I enter sign up username as random_username')
def step_impl(context):
    context.username = generate_random_string(7)
    context.signup_page.enter_username(context.username)


@when(u'I enter sign up password as random_password')
def step_impl(context):
    context.password = generate_random_string(12)
    context.signup_page.enter_password(context.password)

@when(u'I click Sign up button')
def step_impl(context):
    context.signup_page.click_on_signup_button()

@then(u'I should get a sign up error message with text as "{expected_text}"')
def step_impl(context, expected_text):
    assert context.signup_page.verify_error_message_equals(expected_text)

@then(u'I should be navigated to the Login page')
def step_impl(context):
    assert context.login_page.verify_page_is_active()

@when(u'I enter sign up username as "{username}"')
def step_impl(context, username):
    context.signup_page.enter_username(username)

@when(u'I enter sign up password as "{password}"')
def step_impl(context, password):
    context.signup_page.enter_password(password)

@then(u'I should get a sign up username error message with text as "{expected_text}"')
def step_impl(context, expected_text):
   assert context.signup_page.verify_username_error_message(expected_text)

@then(u'I should get a sign up password error message with text as "{expected_text}"')
def step_impl(context, expected_text):
   assert context.signup_page.verify_password_error_message(expected_text)


@when(u'I switch to Login view')
def step_impl(context):
    context.signup_page.click_on_login_view()
    context.login_page = LoginPage(context.driver)
