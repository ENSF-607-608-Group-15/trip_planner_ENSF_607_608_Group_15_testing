from behave import *
from features.pages.LoginPage import LoginPage
from features.pages.MainPage import MainPage
from features.pages.SignupPage import SignupPage


@given(u'I got navigated to Signup page')
def step_impl(context):
    context.signup_page = SignupPage(context.driver)
    assert context.signup_page.check_page_is_active()


@when(u'I click Login button')
def step_impl(context):
    context.main_page = context.login_page.click_on_login_button()


@then(u'I should get redirected to the Sign up page')
def step_impl(context):
    assert context.signup_page.check_page_is_active()


@when(u'I enter password as "{password}"')
def step_impl(context, password):
    context.login_page.enter_password(password)


@then(u'I should get logged in')
def step_impl(context):
    assert context.main_page.verify_user_login()


@when(u'I enter username as "{username}"')
def step_impl(context, username):
    context.login_page.enter_username(username)

@when(u'I switch to Login view')
def step_impl(context):
    context.login_page = context.signup_page.switch_to_login_view()

@then(u'I should get a username error message with text as "{expected_text}"')
def step_impl(context, expected_text):
    assert context.login_page.check_username_error_message(expected_text)


