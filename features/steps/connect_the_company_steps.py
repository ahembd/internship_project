# first open the main page
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import Page
from time import sleep


@given("the user has logged into the main page")
def log_into_reelly(context):
    #store the original window handle so as to show that the window has changed for the next step
    username = 'alhembd@gmail.com'
    password = 'Thomasgoodwin1657*'
    # username = '<USERNAME>'
    # password = '<PASSWORD>'
    context.app.driver.get("https://soft.reelly.io/sign-up")
    # click sign-in link
    sign_in_link = context.driver.find_element(By.CSS_SELECTOR, '.sing-in-text')
    sign_in_link.click()
    context.driver.find_element(By.CSS_SELECTOR, '#email-2').send_keys(username)
    context.driver.find_element(By.CSS_SELECTOR, '#field').send_keys(password)
    # click continue button
    context.driver.find_element(By.XPATH, '//*[@id="wf-form-Sign-up"]/a').click()


@when("the user has Clicked on Connect the company in the left panel")
def connect_the_company_tab(self):
    self.driver.find_element(By.CSS_SELECTOR, 'div.get-free-period.menu').click()
    Page.switch_to_new_window(self)



@then('a new tab opens with a form to register his company')
def new_company_tab(context):
    # original_window = context.driver.current_window_handle
    # old_windows = context.driver.window_handles
    context.driver.find_element(By.CSS_SELECTOR, 'div.get-free-period.menu').click()
    new_window = context.driver.window_handles[1]
    context.driver.switch_to.window(new_window)
    sleep(25)
    print('Just switched tabs, new_company_tab  ' + str(context))
    print('back to original window handle: ' + context.app.driver.window_handles[0])

    context.driver.switch_to.window(context.app.driver.window_handles[0])
    sleep(10)