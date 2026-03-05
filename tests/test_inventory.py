from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_to_cart(page: Page):
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    inventory.assert_on_page()
    inventory.add_all_items_to_cart()
    assert inventory.get_cart_item_count() == inventory.inventory_items.count()

def test_add_single_item_to_cart(page: Page):
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(page)
    inventory.assert_on_page()
    inventory.inventory_items.nth(0).get_by_role("button", name="Add to cart").click()
    assert inventory.get_cart_item_count() == 1

def test_cart_persistence_after_refresh(page: Page):
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    inventory.assert_on_page()
    
    inventory.inventory_items.nth(0).get_by_role("button", name="Add to cart").click()
    expect(inventory.shopping_cart_badge).to_have_text("1")

    page.reload()
    expect(inventory.shopping_cart_badge).to_have_text("1")
    expect(inventory.inventory_items.nth(0).get_by_role("button", name="Remove")).to_be_visible()

def test_remove_from_cart(page: Page):
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    inventory.assert_on_page()
    inventory.add_all_items_to_cart()
    inventory.remove_all_items_from_cart()

    expect(inventory.shopping_cart_badge).not_to_be_visible()

def test_logout(page: Page):
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(page)
    inventory.assert_on_page()
    inventory.logout()
    expect(page).to_have_url("https://www.saucedemo.com/")

