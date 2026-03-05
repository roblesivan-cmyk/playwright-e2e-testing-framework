from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def test_login_success(page: Page):
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    

def test_login_invalid_password(page:Page):
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "wrong_password")
    login.assert_error("Epic sadface: Username and password do not match any user in this service")


def test_login_locked_user(page:Page):
    login = LoginPage(page)
    login.goto()
    login.login("locked_out_user", "secret_sauce")
    login.assert_error("Epic sadface: Sorry, this user has been locked out.")


def test_login_empty_fields(page:Page):
    login = LoginPage(page)
    login.goto()
    login.login("", "")
    login.assert_error("Epic sadface: Username is required")