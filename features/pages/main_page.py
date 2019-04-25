from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class MainPage(BasePage):
    section_flight = (By.ID, "tab-flight-tab-hp")
    dep_place = (By.XPATH, "//*[@id='flight-origin-hp-flight']")
    popup = (By.XPATH, "//div[starts-with(@class, 'autocomplete-dropdown')]")
    dest_place = (By.XPATH, "//*[@id='flight-destination-hp-flight']")
    dep_date = (By.ID, "flight-departing-hp-flight")
    ret_date = (By.ID, "flight-returning-hp-flight")
    button_travellers = (By.XPATH, "//*[@id='traveler-selector-hp-flight']")
    button_search = (By.XPATH, "//*[@id='gcw-flights-form-hp-flight']/div[7]/label/button")

    def _verify_page(self):
        self.on_this_page(self.section_flight, self.dep_place, self.dest_place, self.dep_date, self.ret_date,
                          self.button_travellers, self.button_search)

    def click_to_flights_menu(self):
        self.click_on(self.section_flight)

    def enter_departure_place(self, text):
        self.type_in(self.dep_place, text)

    def click_result_dep(self):
        city_heathrow = (By.XPATH, "//a[contains(@data-value, 'Heathrow')]")
        self.click_on(city_heathrow)

    def enter_destination_place(self, text):
        self.type_in(self.dest_place, text)

    def click_result_dest(self):
        city_dublin = (By.XPATH, "//a[contains(@data-value, 'Dublin')]")
        self.click_on(city_dublin)

    def enter_departure_date(self, text):
        self.type_in(self.dep_date, text)

    def enter_returning_date(self, text):
        self.type_in(self.ret_date, text)

    def click_button_travellers(self):
        self.click_on(self.button_travellers)

    def click_search_button(self):
        self.click_on(self.button_search)
