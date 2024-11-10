from behave import *

@when(u'I enter a departure date as "{departure_date}"')
def step_impl(context, departure_date):
    context.main_page.enter_departure_date(departure_date)
    context.departure_date = departure_date
