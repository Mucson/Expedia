from behave import then

from features.pages.search_results_page import SearchResultsPage


@then("Assert that the price in first row is {price}")
def step_impl(context, price):
    assert price == SearchResultsPage(context.driver).get_first_price()


@then("Assert that the first price is not {price}")
def step_impl(context, price):
    assert price != SearchResultsPage(context.driver).get_first_price()


@then("Assert the visible list of “Airlines included” beneath the list of “Stops”")
def step_impl(context):
    SearchResultsPage(context.driver).is_stops_before_airlines()
