from playwright.sync_api import Page, expect
class InventoryPage:
    URL = "https://www.saucedemo.com/inventory.html"
    def __init__(self, page:Page):
        self.page = page
        self.add_to_cart_buttons = page.locator("button:has-text('Add to cart')")
        self.remove_buttons = page.locator("button:has-text('Remove')")
        self.inventory_items = page.locator(".inventory_item")
        self.shopping_cart_badge = page.locator(".shopping_cart_badge")

        self.menu_button = page.get_by_role("button", name="Open Menu")
        self.all_items_button = page.get_by_role("link", name="All Items")
        self.about_button = page.get_by_role("link", name="About")
        self.logout_button = page.get_by_role("link", name="Logout")
        self.reset_app_state_button = page.get_by_role("link", name="Reset App State")


    def assert_on_page(self):
        expect(self.page).to_have_url(self.URL)


    def add_all_items_to_cart(self):
        count = self.inventory_items.count()
        for i in range(count):
            item = self.inventory_items.nth(i)
            item.get_by_role("button", name="Add to cart").click()

    def remove_all_items_from_cart(self):
        count = self.inventory_items.count()
        for i in range(count):
            item = self.inventory_items.nth(i)
            item.get_by_role("button", name="Remove").click()
        
    def get_cart_item_count(self):
        if self.shopping_cart_badge.is_visible():
            return int(self.shopping_cart_badge.inner_text())
        return 0
    
    def open_cart(self):
        self.shopping_cart_badge.click()
        
    def open_menu(self):
        self.menu_button.click()
        
    def navigate_to_all_items(self):
        self.open_menu()
        self.all_items_button.click()
        
    def navigate_to_about(self):
        self.open_menu()
        self.about_button.click()
        
    def logout(self):
        self.open_menu()
        self.logout_button.click()
    
    def reset_app_state(self):
        self.open_menu()
        self.reset_app_state_button.click()
