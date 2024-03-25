from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)


    def open(self, url):
        self.driver.get(url)


    def find_element(self, *locator):
        return self.driver.find_element(*locator)


    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)


    def click(self, *locator):
        self.driver.find_element(*locator).click()


    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)



    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles  # [window1, window2]
        self.driver.switch_to.window(all_windows[1])
        # use implicit wait so that the tester will see the window



    def switch_to_window_by_id(self, window_id):
        self.driver.switch_to.window(window_id)


    def wait_element_visible(self, *locator):
        print('locator is', *locator)
        self.wait.until(
            EC.visibility_of_element_located(*locator),
            message=f'Element by {locator} is not visible'
        )


    def wait_element_invisible(self, *locator):
        self.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f'Element by {locator} should not be visible'
        )


    def wait_element_clickable(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by {locator} is not clickable'
        )


    def wait_element_clickable_click(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by {locator} is not clickable'
        ).click()

