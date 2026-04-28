from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):

    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    zip_code = (By.ID, "postal-code")
    continue_btn = (By.ID, "continue")
    error_message = (By.CSS_SELECTOR, "h3[data-test='error']")
    finish_btn = (By.ID, "finish")

    success_msg = (By.CLASS_NAME, "complete-header")

    def enter_details(self, fname, lname, zipc):
        self.type(self.first_name, fname)
        self.type(self.last_name, lname)
        self.type(self.zip_code, zipc)        
        
    def click_on_continue(self):
        self.click_btn(self.continue_btn)
        
    def error_msg(self):
        return self.get_text(self.error_message)

    def finish_order(self):
        self.click_btn(self.finish_btn)

    def get_success_message(self):
        return self.get_text(self.success_msg)