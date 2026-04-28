from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):

    add_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
    add_bikelight = (By.ID, "add-to-cart-sauce-labs-bike-light")
    add_tshirt = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    element = (By.ID, "inventory_container")
    apply_filter_path = (By.XPATH, "//select[@class='product_sort_container']")
    item_price_path = (By.XPATH, "//div[@class='inventory_item_price']")
    menu_path = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    logout_path = (By.XPATH, "//a[@id='logout_sidebar_link']")

    def add_product(self):
        self.click_btn(self.add_backpack)
        self.click_btn(self.add_bikelight)
        self.click_btn(self.add_tshirt)
        
    def inventory_page_title(self):
        return self.get_title_of_the_page("Swag Labs")
    
    def inventory_page_url(self):
        url = "https://www.saucedemo.com/inventory.html"
        return self.get_page_url(url)
    
    def inventory_page_element(self):
        return self.validate_element_of_page(self.element)
    
    def go_to_cart(self):
        self.click_btn(self.cart_icon)
        
    def apply_filter(self, value):
        select_value = self.select_dropdown(self.apply_filter_path)
        return select_value.select_by_value(value)
    
    def extract_items_price_and_sort(self):
        elements = self.driver.find_elements(*self.item_price_path)
        price_list = []
        for element in elements:
            price_list.append(element.text.strip())
        original_list = [float(p.replace('$', '')) for p in price_list]
        # print(f"Original List: {original_list}")
        sorted_list = sorted(original_list)
        # print(f"Sorted List: {sorted_list}")
        return original_list, sorted_list
    
    def open_menu_and_logout(self):
        self.click_btn(self.menu_path)
        self.click_btn(self.logout_path)
        
    def login_page_url(self):
        url = "https://www.saucedemo.com/"
        return self.get_page_url(url)
        
    
    
        
        