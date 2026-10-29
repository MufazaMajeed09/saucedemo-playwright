import pytest
from playwright.sync_api import expect, Page
from pages.login_page import LoginPage

@pytest.fixture
def logged_in(page:Page):


    login_page = LoginPage(page)
    login_page.open_login_page()
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.press_login()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator('[data-test="title"]')).to_have_text("Products")

    return page



