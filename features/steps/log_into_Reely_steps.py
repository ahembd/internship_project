from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import Page
import logging

use_step_matcher("re")


@given("that the user has logged into the main page")
def log_into_reelly(context):
    # store the original window handle so as to show that the window has changed for the next step
    username = 'roggertorrez@yaoghyth.cz'
    password = 'GeorgeWashington'
    # username = '<USERNAME>'
    # password = '<PASSWORD>'
    context.app.driver.get("https://soft.reelly.io/sign-up")
    print('logging into sign-in page')
    # click sign-in link
    sign_in_link = context.driver.find_element(By.CSS_SELECTOR, '.sing-in-text')
    sign_in_link.click()
    context.driver.find_element(By.CSS_SELECTOR, '#email-2').send_keys(username)
    context.driver.find_element(By.CSS_SELECTOR, '#field').send_keys(password)
    print('just entered username and password')
    # click continue button
    context.driver.find_element(By.XPATH, '//*[@id="wf-form-Sign-up"]/a').click()


@when("the user clicks Bali")
def user_selects_bali(self):
    locator = (By.CSS_SELECTOR, 'h2.h2-partner-card')
    self.wait.until(
        EC.visibility_of_element_located(locator),
        message=f'Element by {locator} is not visible')
    self.driver.find_element(By.CSS_SELECTOR, 'h2.h2-partner-card').click()
    print('past call to view Bali properties')
    all_windows = self.driver.window_handles  # [window1, window2]
    self.driver.switch_to.window(all_windows[0])


@then("properties in Bali which are in the system will appear")
def step_impl(context):
    pass
    # assert "/book-presentation" in context.driver.current_url, f"Expected '/book-presentation' in {context.driver.current_url}"


# @when("the user chooses construction date of 4Q 2024")
# def user_chooses_construction_date(context):
#     completion_data_lst = context.driver.find_elements_by_xpath("('#comletion-select-2')").click()
#     assert completion_data_lst == '4Q 2024', 'Construction date does not equal 4Q 2024'
#
# @then("properties that will have been completed prior to 4Q 2024 will appear")
# def select_properties_before_fourth_quarter_of_2024(context):
#     pass
#
#
# @when("the user selects value ranges from 600000 AED to 1.5 million AED")
# def select_value_of_properties_between_60000_and_1_and_a_half_million(context):
#     pass
#
#
# @then("properties in Bali within that value range will appear")
# def verify_properties_in_above_value_range(context):
#     pass
#
#
# @when("the user selects property type of 'Apartment'")
# def set_filter_for_apartments(context):
#     pass
#
#
# @then("apartments will appear")
# def verify_only_apartments_appear(context):
#     pass
#
#
# @when("the user chooses 'Penthouse'")
# def set_filter_for_penthouses(context):
#     pass
#
#
# @then("penthouses will appear")
# def verify_only_apartments_appear(context):
#     pass
#
#
