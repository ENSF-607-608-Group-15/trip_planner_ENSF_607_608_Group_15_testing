from behave import *
from features.pages.LoginPage import LoginPage
from features.pages.SignupPage import SignupPage


@given(u'I got navigated to Login page')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    assert context.login_page.verify_page_is_active()


@when(u'I click Login button')
def step_impl(context):
    context.main_page = context.login_page.click_on_login_button()


@then(u'I should get a login error message with text as "{expected_text}"')
def step_impl(context, expected_text):
    assert context.login_page.verify_error_message_equals(expected_text)


@when(u'I enter login password as "{password}"')
def step_impl(context, password):
    context.login_page.enter_password(password)


@then(u'I should get logged in')
def step_impl(context):
    assert context.main_page.verify_user_login()


@when(u'I enter login username as "{username}"')
def step_impl(context, username):
    context.login_page.enter_username(username)


@then(u'I should get a login username error message with text as "{expected_text}"')
def step_impl(context, expected_text):
    assert context.login_page.verify_username_validation_message(expected_text)


@when(u'I click Continue as Guest button')
def step_impl(context):
    context.main_page = context.login_page.click_on_guest_button()


@when(u'I switch to Sign up view')
def step_impl(context):
    context.login_page.click_on_signup_view()
    context.signup_page = SignupPage(context.driver)


@when(u'I enter login username')
def step_impl(context):
    context.login_page.enter_username(context.username)


@when(u'I enter login password')
def step_impl(context):
    context.login_page.enter_password(context.password)
    