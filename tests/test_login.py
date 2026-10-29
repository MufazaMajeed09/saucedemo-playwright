from playwright.sync_api import expect, Page
from pages.login_page import LoginPage
import pytest

def test_valid_login(page:Page):
    # page.goto("https://www.saucedemo.com/")
    # page.locator('[data-test="username"]').fill("standard_user")
    # page.locator('[data-test="password"]').fill("secret_sauce")
    # page.locator('[data-test="login-button"]').click()
    login_page = LoginPage(page)
    login_page.open_login_page()
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.press_login()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator('[data-test="title"]')).to_have_text("Products")

@pytest.mark.parametrize("username,password,expected_value" ,
[
    ("standard_user","wrong123","Epic sadface: Username and password do not match any user in this service"),
    ("locked_out_user","secret_sauce","Epic sadface: Sorry, this user has been locked out."),
    ("" , "", "Epic sadface: Username is required")
])
def test_invalid_login(page:Page,username,password,expected_value):
    login_page = LoginPage(page)
    login_page.open_login_page()


    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.press_login()


    expect (login_page.error_text).to_have_text(expected_value)

def test_logout(logged_in):
    login_page = LoginPage(logged_in)
    logged_in.locator("#react-burger-menu-btn").click()
    logged_in.locator('[data-test="logout-sidebar-link"]').click()
    expect(logged_in).to_have_url("https://www.saucedemo.com/")
    expect(login_page.username).to_be_visible()






     

        
