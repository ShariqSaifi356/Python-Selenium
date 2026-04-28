import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.data_reader import test_list

@pytest.mark.parametrize("test_list_items", test_list[:1])
def test_checkout_flow(setup, test_list_items):
    driver = setup

    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    # Login
    # Passing data through JSON
    login.login(test_list_items["username"], test_list_items["password"])
    
    
    # Checking Title of the page
    assert inventory.inventory_page_title() == "Swag Labs"
    
    # Checking URL of the page
    assert inventory.inventory_page_url() == "https://www.saucedemo.com/inventory.html"
    
    # Checking element is visible or not 
    assert inventory.inventory_page_element().is_displayed()