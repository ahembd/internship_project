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
    username = 'roggertorrez@yaoghyth.cz'
    password = 'GeorgeWashington'
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
    # print('in connect_the_company_tab')
    # print('presently on page ' + self.driver.current_window_handle)
    # print(str('window handles are ' + str(self.driver.window_handles)))
    Page.wait_element_visible(self, (By.CSS_SELECTOR, 'div.get-free-period.menu'))
    # print('past wait element visible')
    self.driver.find_element(By.CSS_SELECTOR, 'div.get-free-period.menu').click()
    # print('past call to click div.get-free-period.menu')


@then('a new tab opens with a form to register his company')
def new_company_tab(context):
    context.driver.find_element(By.CSS_SELECTOR, 'div.get-free-period.menu').click()
    new_window = context.driver.window_handles[1]
    context.driver.switch_to.window(new_window)
    assert "/book-presentation" in context.driver.current_url, f"Expected '/book-presentation' in {context.driver.current_url}"
    # Thanks so much for the assertion statement, Jefferson!
    print('Just switched tabs, new_company_tab  ' + str(context))
    print('back to original window handle: ' + context.app.driver.window_handles[0])

    context.driver.switch_to.window(context.app.driver.window_handles[0])