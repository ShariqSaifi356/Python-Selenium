from playwright.sync_api import Page


def test_login(page: Page):
    page.goto("https://www.saucedemo.com/")
    assert "Swag Labs" in page.title()