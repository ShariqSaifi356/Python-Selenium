import pytest
from pages.login_page import LoginPage
from utils.data_reader import test_list_2

@pytest.mark.parametrize("test_list_items", test_list_2)
def test_checkout_flow(setup, test_list_items):
    driver = setup

    login = LoginPage(driver)

    # Login should be failed
    # Passing data through JSON
    login.login(test_list_items["username"], test_list_items["password"])
    
    assert "Epic sadface:" in login.login_failed_error()