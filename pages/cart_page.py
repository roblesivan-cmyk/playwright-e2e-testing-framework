from playwright.sync_api import Page, expect


class CartPage:
    URL = "https://www.saucedemo.com/cart.html"


    def __init__(self, page:Page):
        self.page = page
        self.cart_items = page.locator(".cart_item")
        self.checkout_button = page.get_by_role("button", name="Checkout")
        self.continuie_shopping_button = page.get_by_role("button", name="Continue Shopping")

    def goto(self):
        self.page.goto(self.URL)

    def assert_on_page(self):
        expect(self.page).to_have_url(self.URL)
        expect(self.checkout_button).to_be_visible()

    def get_cart_item_count(self):
        return self.cart_items.count()
    
    def checkout(self):
        self.checkout_button.click()
    
    def continue_shopping(self):
        self.continuie_shopping_button.click()