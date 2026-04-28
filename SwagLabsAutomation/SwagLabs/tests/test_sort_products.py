import time

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
    
    inventory.apply_filter("lohi")
    
    original_list, sorted_list = inventory.extract_items_price_and_sort()
    assert original_list == sorted_list, "Prices are not sorted correctly"