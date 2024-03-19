# first open the main page
from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


@given("the user has logged into the main page")
def log_into_reelly(context):
    username = 'alhembd@gmail.com'
    password = 'Thomasgoodwin1657*'
    # username = '<USERNAME>'
    # password = '<PASSWORD>'
    context.driver.get("https://soft.reelly.io/sign-up")
    # click sign-in link
    sign_in_link = context.driver.find_element(By.XPATH, '//*[@id="wf-form-Create-account"]/a[1]/div[2]')
    sign_in_link.click()
    context.driver.find_element(By.CSS_SELECTOR, '#email-2').send_keys(username)
    context.driver.find_element(By.CSS_SELECTOR, '#field').send_keys(password)
    # click continue button
    context.driver.find_element(By.XPATH, '//*[@id="wf-form-Sign-up"]/a').click()


@when("the user has Clicked on Connect the company in the left panel")
def connect_the_company_tab(context):
    context.driver.find_element(By.XPATH, '//*[@id="w-node-_99a5c496-8f77-9959-16dd-e8eb9b22b68b-9b22b68b"]/div[2]/a').click()


@then('a new tab opens with a form to register his company')
def new_company_tab(context):
    pass