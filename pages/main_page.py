from pages.base_page import Page
from time import sleep
from selenium.webdriver.common.by import By


class MainPage(Page):

    SEARCH_FIELD = (By.CSS_SELECTOR, '#field-6')
    FILTER_BTN = (By.CSS_SELECTOR, '#wf-form-Search-form')

    def open_main(self):
        self.driver.get('https://soft.reelly.io/off-plan')

    def search(self, item):
        self.input_text(item, *self.SEARCH_FIELD)
        self.click(*self.FILTER_BTN)
        sleep(6)  # wait for ads to disappear