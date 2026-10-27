from playwright.sync_api import expect, Page
import pytest;

def test_valid_login(page:Page):
    page.goto("https://www.saucedemo.com/")
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()
  

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator('[data-test="title"]')).to_have_text("Products")

@pytest.mark.parametrize("username,password,expected_value" ,
[
    ("standard_user","wrong123","Epic sadface: Username and password do not match any user in this service"),
    ("locked_out_user","secret_sauce","Epic sadface: Sorry, this user has been locked out."),
    ("" , "", "Epic sadface: Username is required")
])
def test_invalid_login(page:Page,username,password,expected_value):
    page.goto("https://www.saucedemo.com/")
    page.locator('[data-test="username"]').fill(username)
    page.locator('[data-test="password"]').fill(password)
    page.locator('[data-test="login-button"]').click()

    expect (page.locator('[data-test="error"]')).to_have_text(expected_value)






     

        
