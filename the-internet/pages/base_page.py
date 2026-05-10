from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
    def click_on_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()     
        
    def validate_element_of_page(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))