import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.data_reader import test_list

@pytest.mark.parametrize("test_list_items", test_list[:1])
def test_checkout_flow(setup, test_list_items):
    driver = setup

    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    # Login
    # Passing data through JSON
    login.login(test_list_items["username"], test_list_items["password"])

    # Add product
    inventory.add_product()

    # Go to cart
    inventory.go_to_cart()

    # Checkout
    cart.click_checkout()

    checkout.click_on_continue()

    assert "Error:" in checkout.error_msg()