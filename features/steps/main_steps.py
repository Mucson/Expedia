from behave import *
import time
from features.pages.main_page import MainPage


@step("I open main page")
def step_impl(context):
    context.driver.get("https://www.expedia.com/")


@when("I select Flights")
def step_impl(context):
    main_page = MainPage(context.driver)
    main_page.click_to_flights_menu()


@then('I type {city} in Flying from field and select {airport}')
def step_impl(context, city, airport):
    main_page = MainPage(context.driver)
    time.sleep(2)
    main_page.enter_departure_place(city)
    main_page.click_result_dep()


@then('I type {city} in Flying to field and select {airport}')
def step_impl(context, city, airport):
    main_page = MainPage(context.driver)
    main_page.enter_destination_place(city)
    main_page.click_result_dest()


@then("Select Departing: {date}")
def step_impl(context, date):
    main_page = MainPage(context.driver)
    main_page.enter_departure_date(date)


@then("Select Returning: {date}")
def step_impl(context, date):
    main_page = MainPage(context.driver)
    main_page.enter_returning_date(date)


@then("I pick two adult")
def step_impl(context):
    main_page = MainPage(context.driver)
    main_page.click_button_travellers()

    main_page.field_person = main_page.driver.find_element_by_xpath(
        "//*[@id='traveler-selector-hp-flight']/div/ul/li/div/div/div/div[1]/div[4]/button")
    main_page.field_person.click()

    main_page.btn_close = main_page.driver.find_element_by_xpath(
        "//*[@id='traveler-selector-hp-flight']/div/ul/li/div/footer/div/div[2]/button")
    main_page.btn_close.click()


@then("I click search button")
def step_impl(context):
    main_page = MainPage(context.driver)
    main_page.click_search_button()
