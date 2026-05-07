from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ABTestingPage(BasePage):

    element = (By.XPATH, "//a[normalize-space()='A/B Testing']")

    def openABTestingPage(self):
        self.click_on_element(self.element)