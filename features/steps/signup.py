from behave import *
from features.pages.LoginPage import LoginPage
from features.pages.MainPage import MainPage
from features.pages.SignupPage import SignupPage

@given(u'I am on the Login page')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    assert context.login_page.check_page_is_active()


@when(u'I click sign up button')
def step_impl(context):
    context.login_page.click_on_signup_button()


@then(u'I should be navigated to the sign up page')
def step_impl(context):
    context.signup_page = SignupPage(context.driver)
    assert context.signup_page.check_page_is_active()


@then(u'I enter username as random_username')
def step_impl(context):
    random_username = SignupPage.random_generator()
    context.signup_page.enter_username(random_username)


@then(u'I enter password as random_password')
def step_impl(context):
    random_password = SignupPage.random_generator()
    context.signup_page.enter_username(random_password)

@then(u'I click sign up botton')
def step_impl(context):
    context.signup_page.click_on_signup_button()

@then(u'I should get error message with text as "{expected_text}"')
def step_impl(context, expected_text):
    assert context.signup_page.check_username_error_message(expected_text)

@then(u'I should be navigated back to the login page')
def step_impl(context):
    context.login_page = context.signup_page.switch_to_login_view()
    assert context.login_page.check_page_is_active()

@then(u'I enter username as "{username}"')
def step_impl(context, username):
    context.signup_page.enter_username(username)

@then(u'I enter password as "{password}"')
def step_impl(context, password):
    context.signup_page.enter_password(password)

@then(u'I should get username error message with text as "{expected_text}"')
def step_impl(context, expected_text):
   assert context.signup_page.check_username_error_message(expected_text)

@then(u'I should get password error message with text as "{expected_text}"')
def step_impl(context, expected_text):
   assert context.signup_page.check_password_error_message(expected_text)

@then(u'I should see confirm message with text as "{expected_text}"')
def step_impl(context):
    pass