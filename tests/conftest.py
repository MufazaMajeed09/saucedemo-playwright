import pytest
from playwright.sync_api import expect, Page
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

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



@pytest.fixture
def checkout(logged_in):
    
    products_page = ProductsPage(logged_in)
    products_page.add_bag_pack()

    products_page.click_cart_button() 

    #new web page means new object class
    cart_page = CartPage(logged_in)
    cart_page.click_checkout_button()

    #new web page
    checkout_page = CheckoutPage(logged_in)

    return logged_in