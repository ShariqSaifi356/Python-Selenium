from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):

    checkout_btn = (By.ID, "checkout")
    remove_btns = (By.XPATH, "//button[contains(@class, 'cart_button')]")

    def click_checkout(self):
        self.click_btn(self.checkout_btn)
        
    def click_remove_btn(self):
        super().click_multiple_btn(self.remove_btns)
    
    def check_cart_count(self):
        cart_element_count = self.driver.find_elements(By.XPATH, "//div[@id='shopping_cart_container']/a/span")
        return cart_element_count