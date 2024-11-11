from behave import *
from features.pages.LoginPage import LoginPage
from features.pages.MainPage import MainPage

@then(u'I should be navigated to the main page')
def step_impl(context):
    context.main_page = MainPage(context.driver)
    assert context.main_page.verify_user_login

@when(u'I enter departure city as "{departure_city}"')
def step_impl(context, departure_city):
    context.main_page.enter_departure_city(departure_city)
    context.departure_city = departure_city

@when(u'I enter departure date as "{departure_date}"')
def step_impl(context, departure_date):
      context.main_page.enter_departure_date(departure_date)
      context.departure_date = departure_date
 
@when(u'I enter return date as "{return_date}"')
def step_impl(context, return_date):
    context.main_page.enter_return_date(return_date)
    context.return_date = return_date

@when(u'I enter desired trip location as "{desired_location}"')
def step_impl(context, desired_location):
    context.main_page.enter_desired_location(desired_location)
    context.desired_location = desired_location

@when(u'I enter a budget limit of "{budget}"')
def step_impl(context, budget):
   context.main_page.enter_budget(budget)
   context.budget = budget

@when(u'I enter a theme as "{theme}"')
def step_impl(context, theme):
    context.main_page.enter_theme(theme)
    context.theme = theme

@when(u'I click Generate My Trip button')
def step_impl(context):
   context.main_page.click_on_generate_trip_button()


@then(u'I should see the vacation planning details')
def step_impl(context):
    assert context.main_page.verify_plan_content_is_active()


@when(u'I enter username as "{username}"')
def step_impl(context, username):
    context.login_page.enter_username(username)


@when(u'I enter password as "{password}"')
def step_impl(context, password):
    context.login_page.enter_password(password)

@when(u'I click the Previous Vacation Plans button')
def step_impl(context):
    context.main_page.click_on_previous_plan_button()


@then(u'I should see a list of previously generated plans')
def step_impl(context):
    assert context.main_page.verify_previous_plan_is_active()


@when(u'I select the family-friendly option')
def step_impl(context):
    context.main_page.click_on_family_friendly_checkbox()

@when(u'I select the no-flying option')
def step_impl(context):
    context.main_page.click_on_no_flying_checkbox()


@when(u'I select the disability-friendly option')
def step_impl(context):
    context.main_page.click_on_disability_friendly_checkbox()


@when(u'I select the group discount option')
def step_impl(context):
    context.main_page.click_on_group_discount_checkbox()

@then(u'I should see vacation plan suggestions related to "{keywords}"')
def step_impl(context, keywords):
    keywords_list = [keyword.strip() for keyword in keywords.split(",")]
    assert context.main_page.verify_suggestions_text_contain(keywords_list)