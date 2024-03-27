from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from support.logger import logger


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

###########################################
    ##### For running in Firefox ##########
    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)
    # print('Gecko driver installed.')
    #
    # firefox_options = webdriver.FirefoxOptions()
    # firefox_options.add_argument('--window-size=1920x1080')
    # # firefox_options.add_argument('headless')
    #
    # # BROWSERS WITH DRIVERS: provide path to the driver file ###
    # service = Service(executable_path='/Users/alberthembd/Desktop/internship_project/.venv/geckodriver')
    # context.driver = webdriver.Firefox(service=service)
    # print('Firefox driver == ' + str(context.driver))
    # print('past setting service and driver for Firefox.')

    ### SAFARI ###
    # context.driver = webdriver.Safari()

    ### HEADLESS MODE IN CHROME ####
    ## print('about to assign the value of service')
    # service = Service(ChromeDriverManager().install())
    # print('service = {}'.format(service))
    # context.driver = webdriver.Chrome(
    #    options=options,
    #     service=service
    #)


    ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user = 'alberthembd_KDjYed'
    # bs_key = 'YVWXkX9EghNgc7X5yLDo'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     'os': 'Windows',
    #     'osVersion': '10',
    #     'browserName': 'Firefox',
    #     'sessionName': scenario_name
    # }
    #
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()

    context.driver.implicitly_wait(4)
    context.wait = WebDriverWait(context.driver, 15)
    context.app = Application(context.driver)

def before_scenario(context, scenario):
    # print('\nStarted scenario: ', scenario.name)
    logger.info(f'\nStarted scenario: {scenario.name}')
    logger.info(f'about to call browser_init a second time, scenario_name is: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    logger.info(f'\nStarted step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        # Screenshot:
        # context.driver.save_screenshot(f'step_failed_{step}.png')
        logger.info(f'\nStep failed: {step}')


def after_scenario(context, feature):
    context.driver.quit()



