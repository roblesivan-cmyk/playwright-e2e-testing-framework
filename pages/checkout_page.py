from playwright.sync_api import Page, expect


class CheckoutPage:
    INFO_URL = "https://www.saucedemo.com/checkout-step-one.html"
    OVERVIEW_URL = "https://www.saucedemo.com/checkout-step-two.html"
    COMPLETE_URL = "https://www.saucedemo.com/checkout-complete.html"

    def __init__(self, page:Page):

        # Step One
        self.page = page
        self.first_name_input = page.get_by_role("textbox", name="First Name")
        self.last_name_input = page.get_by_role("textbox", name="Last Name")
        self.postal_code_input = page.get_by_role("textbox", name="Zip/Postal Code")
        self.continue_button = page.get_by_role("button", name="Continue")
        self.cancel_button = page.get_by_role("button", name="Cancel")
        self.error_message = page.locator("[data-test='error']")
        
        # Step Two
        self.finish_button = page.locator("[data-test='finish']")
        self.total_label = page.locator(".summary_total_label")

        #Complete
        self.complete_header = page.locator(".complete-header")

        # ---------- Step One ----------
    def assert_on_info(self):
        expect(self.page).to_have_url(self.INFO_URL)
        expect(self.continue_button).to_be_visible()

    def fill_info(self, first_name: str, last_name: str, postal_code: str):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)

    def continue_to_overview(self):
        self.continue_button.click()

    def assert_error(self, text: str):
        expect(self.error_message).to_be_visible()
        expect(self.error_message).to_have_text(text)

    # ---------- Step Two ----------
    def assert_on_overview(self):
        expect(self.page).to_have_url(self.OVERVIEW_URL)
        expect(self.finish_button).to_be_visible()

    def finish(self):
        self.finish_button.click()

    def get_total_text(self) -> str:
        return self.total_label.inner_text()

    # ---------- Complete ----------
    def assert_complete(self):
        expect(self.page).to_have_url(self.COMPLETE_URL)
        expect(self.complete_header).to_be_visible()