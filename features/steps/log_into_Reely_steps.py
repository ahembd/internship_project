from behave import *
from selenium.webdriver.common.by import By
from time import sleep

from pages.main_page import MainPage
from pages.base_page import Page
use_step_matcher("re")


@given("that the user has logged into https://soft.reelly.io/off-plan")
def log_into_reelly(context):
    username = 'alhembd@gmail.com'
    password = 'Thomasgoodwin1657*'
    context.driver.get("https://soft.reelly.io/sign-up")
    # click sign-in link
    sign_in_link = context.driver.find_element(By.XPATH, '//*[@id="wf-form-Create-account"]/a[1]/div[2]')
    sign_in_link.click()
    context.driver.find_element(By.CSS_SELECTOR, ('#email-2')).send_keys(username)
    context.driver.find_element(By.CSS_SELECTOR, ('#field')).send_keys(password)
    # continue button
    continue_button = context.driver.find_element(By.XPATH, '//*[@id="wf-form-Sign-up"]/a').click()

    # BALI_SELECTOR = context.driver.find_element(By.XPATH, ('//*[@id="w-node-a12e6235-4ea1-44ef-5a02-9f96ec022f3d-7f66de48"]/a/h2'))
    # BALI_SELECTOR.click()



@when("the user clicks Bali")
def user_selects_bali(context):
    BALI_BTN = (By.XPATH, '//*[@id="w-node-b3e2d1dd-1dc5-4f3f-14dd-85ad6c4b0445-7f66df20"]/div[2]/div[2]/div[5]/div[3]/div')
    sleep(15)


@then("properties in Bali which are in the system will appear")
def step_impl(context):
    pass


@when("the user chooses construction date of 4Q 2024")
def user_chooses_construction_date(context):
    completion_data_lst = context.driver.find_elements_by_xpath("('#comletion-select-2')").click()
    assert completion_data_lst == '4Q 2024', 'Construction date does not equal 4Q 2024'

@then("properties that will have been completed prior to 4Q 2024 will appear")
def select_properties_before_fourth_quarter_of_2024(context):
    pass


@when("the user selects value ranges from 600000 AED to 1.5 million AED")
def select_value_of_properties_between_60000_and_1_and_a_half_million(context):
    pass


@then("properties in Bali within that value range will appear")
def verify_properties_in_above_value_range(context):
    pass


@when("the user selects property type of 'Apartment'")
def set_filter_for_apartments(context):
    pass


@then("apartments will appear")
def verify_only_apartments_appear(context):
    pass


@when("the user chooses 'Penthouse'")
def set_filter_for_penthouses(context):
    pass


@then("penthouses will appear")
def verify_only_apartments_appear(context):
    pass
