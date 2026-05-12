from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ABTestingPage(BasePage):

    element = (By.XPATH, "//a[normalize-space()='A/B Testing']")
    body_of_webpage = (By.XPATH, "//body")
    heading  = (By.TAG_NAME, "h3")

    def openABTestingPage(self):
        self.click_on_element(self.element)
        
    def visibilityOfElement(self):
        return self.validate_element_of_page(self.body_of_webpage).is_displayed()
    
    def url(self):
        return self.get_page_url(self.driver.current_url)
    
    def headingOfABPage(self):
        return self.get_text(self.heading)