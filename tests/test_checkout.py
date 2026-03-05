from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout_happy_path(page: Page):
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    inventory.assert_on_page()
    inventory.inventory_items.nth(0).get_by_role("button", name="Add to cart").click()
    expect(inventory.shopping_cart_badge).to_have_text("1")

    inventory.open_cart()
    cart = CartPage(page)
    cart.assert_on_page()
    expect(cart.cart_items).to_have_count(1)
    cart.checkout()

    checkout = CheckoutPage(page)
    checkout.assert_on_info()
    checkout.fill_info("Ivan", "Test", "50000")
    checkout.continue_to_overview()

    checkout.assert_on_overview()
    expect(page.locator(".summary_total_label")).to_be_visible()
    checkout.finish()

    checkout.assert_complete()


def test_checkout_missing_postal_code_shows_error(page: Page):
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    inventory.assert_on_page()
    inventory.inventory_items.nth(0).get_by_role("button", name="Add to cart").click()

    inventory.open_cart()
    cart = CartPage(page)
    cart.assert_on_page()
    cart.checkout()

    checkout = CheckoutPage(page)
    checkout.assert_on_info()
    checkout.fill_info("Ivan", "Test", "")
    checkout.continue_to_overview()

    checkout.assert_error("Error: Postal Code is required")