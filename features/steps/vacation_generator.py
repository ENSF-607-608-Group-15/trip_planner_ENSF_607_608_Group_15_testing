from behave import *


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


@when(u'I enter a trip theme as "{theme}"')
def step_impl(context, theme):
    context.main_page.enter_theme(theme)
    context.theme = theme


@when(u'I click Generate My Trip button')
def step_impl(context):
    context.main_page.click_on_generate_trip_button()


@then(u'I should see the vacation planning details')
def step_impl(context):
    assert context.main_page.verify_plan_content_is_active()


@when(u'I click the Previous Vacation Plans button')
def step_impl(context):
    context.main_page.click_on_previous_plan_button()


@when(u'I click the Previous Settings button')
def step_impl(context):
    context.main_page.click_on_previous_settings_button()


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


@then(u'I should see vacation plan suggestions not related to "{keywords}"')
def step_impl(context, keywords):
    keywords_list = [keyword.strip() for keyword in keywords.split(",")]
    assert context.main_page.verify_suggestions_text_not_contain(keywords_list)


@then(u'I should see an error popup indicating "{error_message}"')
def step_impl(context, error_message):
    assert context.main_page.verify_error_popup(error_message)


@then(u'I should get a return date error message with text as "{expected_text}"')
def step_impl(context, expected_text):
    assert context.main_page.verify_return_date_error_message(expected_text)


@then(u'I should see a PDF download link')
def step_impl(context):
    assert context.main_page.verify_pdf_download_link_exists()


@then(u'I should see required field error messages for inputs "{keywords}"')
def step_impl(context, keywords):
    keywords_list = [keyword.strip() for keyword in keywords.split(",")]
    assert context.main_page.verify_trip_error_message_contains(keywords_list)


@then(u'I should see a table of my previous trip settings containing "{keywords}"')
def step_impl(context, keywords):
    keywords_list = [keyword.strip() for keyword in keywords.split(",")]
    assert context.main_page.verify_trip_previous_settings_contains(keywords_list)