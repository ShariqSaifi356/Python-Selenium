from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ABTestingPage(BasePage):

    element = (By.XPATH, "//a[normalize-space()='A/B Testing']")
    body_of_webpage = (By.XPATH, "//body")

    def openABTestingPage(self):
        self.click_on_element(self.element)
        
    def visibilityOfElement(self):
        return self.validate_element_of_page(self.body_of_webpage).is_displayed()