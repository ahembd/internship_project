from pages.base_page import Page
from selenium.webdriver.common.by import By
# from pages.header import Header
from time import sleep
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage


class Header(Page):
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_ICON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")

    def search_product(self):
        self.input_text('coffee', *self.SEARCH_FIELD)
        self.click(*self.SEARCH_ICON)
        sleep(6)

    def click_cart_icon(self):
        self.wait_element_clickable_click(*self.CART_ICON)