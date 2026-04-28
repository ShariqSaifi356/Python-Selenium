from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_btn(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        
    def click_multiple_btn(self, locator):
        elements = self.driver.find_elements(*locator)
        for element in elements:
            element.click()

    def type(self, locator, value):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(value)

    def get_text(self, locator):
        text = self.wait.until(EC.visibility_of_element_located(locator)).text
        return text
    
    def get_title_of_the_page(self, title_of_webpage):
        self.wait.until(EC.title_is(title_of_webpage))
        return self.driver.title
    
    def get_page_url(self, url_of_webpage):
        self.wait.until(EC.url_to_be(url_of_webpage))
        return self.driver.current_url
    
    def validate_element_of_page(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
        
    def select_dropdown(self, locator):
        select_element = Select(self.wait.until(EC.element_to_be_clickable(locator)))
        return select_element
        