from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class CirclePage(Page):
    TABS = (By.CSS_SELECTOR, "[class*='PageSelectionText'] a")
    BONUS_TAB = (By.CSS_SELECTOR, "[data-test='bonus-tab']")
    GOOGLE_PLAY_BTN = (By.CSS_SELECTOR, "[alt='Get it on Google Play']")

    def open_circle(self):
        self.open('https://www.target.com/circle')

    def click_google_play_btn(self):
        print(' in click_google_play_btn')
        self.wait_element_clickable_click(*self.GOOGLE_PLAY_BTN)

    def verify_google_play_opened(self):
        print('in verify_google_play_opened')
        self.verify_partial_url('https://play.google.com/store/apps/')
        print('past call to verify_partial_url')

    # def wait_url_changes(self, current_url):
    #     Page.wait_url_changes(self, current_url)

    def verify_can_click_thru_tabs(self):
        self.wait_element_clickable(*self.BONUS_TAB)
        tabs = self.find_elements(*self.TABS)
        current_url = ''
        for i in range(len(tabs)):
            # Search for tabs before every click to avoid StaleElementReferenceException
            tabs = self.find_elements(*self.TABS)
            print('tabs are ' + str((tabs)))
            tabs[i].click()
            current_url = self.driver.current_url
            print('current url is ' + str(current_url))
            self.wait_url_changes(current_url)

    def verify_partial_url(self, current_url):
        self.verify_partial_url(current_url)
