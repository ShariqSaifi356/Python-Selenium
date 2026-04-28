from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_btn = (By.ID, "login-button")
    login_failed_error_msg = (By.CSS_SELECTOR, "h3[data-test='error']")

    def login(self, user, pwd):
        self.type(self.username, user)
        self.type(self.password, pwd)
        self.click_btn(self.login_btn)
            
    def login_failed_error(self):
        return self.get_text(self.login_failed_error_msg)