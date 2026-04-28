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
    
    # Step 2: Validate inventory page loaded
    assert inventory.is_inventory_page_visible()

    # Step 3: Delete cookies (SESSION BREAK)
    driver.delete_all_cookies()

    # Step 4: Try to access inventory page again
    driver.get("https://www.saucedemo.com/inventory.html")

    # Step 5: Validate redirected to login page
    current_url = driver.current_url

    assert "saucedemo.com" in current_url
    assert "inventory" not in current_url

    