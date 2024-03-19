from pages.base_page import Page
from pages.main_page import MainPage
from pages.header import Header


class Application:
    def __init__(context, driver):
        context.page = Page(driver)
        context.header = Header(driver)
        context.main_page = MainPage(driver)
        context.driver = driver
