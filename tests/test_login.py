import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.fixture
def page(playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    yield page
    browser.close()

def test_successful_login(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)

    login.open()
    login.login("standard_user", "secret_sauce")

    assert inventory.is_opened()

def test_wrong_password(page):
    login = LoginPage(page)

    login.open()
    login.login("standard_user", "wrong_password")

    assert "Username and password do not match" in login.get_error_text()

def test_locked_out_user(page):
    login = LoginPage(page)

    login.open()
    login.login("locked_out_user", "secret_sauce")

    assert "locked out" in login.get_error_text().lower()

def test_empty_fields(page):
    login = LoginPage(page)

    login.open()
    login.login("", "")

    assert "required" in login.get_error_text().lower()

def test_performance_glitch_user(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)

    login.open()
    login.login("performance_glitch_user", "secret_sauce")

    page.wait_for_url("**/inventory.html", timeout=10000)
    assert inventory.is_opened()