from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class SearchResultsPage(BasePage):
    first_price = (By.XPATH, "//span[@data-test-id='listing-price-dollars']")

    def _verify_page(self):
        self.on_this_page(self.first_price)

    def get_first_price(self):
        return self.get_text(self.first_price)

    list_field = (By.XPATH, "//div[@id='filter-container']")
    index_stops = (By.XPATH, "//legend[contains(@id, 'stops')]")
    index_service = (By.XPATH, "//legend[contains(@id, 'airlines')]")

    def is_stops_before_airlines(self):
        headers = self.driver.find_elements(By.XPATH, "//legend[@class = 'section-header-sub']")
        list_headers = []
        for header in headers:
            list_headers.append(header.text)
        assert list_headers.index("Stops") < list_headers.index("Airlines included")
