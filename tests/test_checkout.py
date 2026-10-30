from playwright.sync_api import expect, Page
import pytest
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.finish_checkout_page import FinishCheckoutPage
from pages.checkout_complete import CheckOutCompletePage

def test_check_out(logged_in):
    products_page = ProductsPage(logged_in)
    products_page.add_bag_pack()

    products_page.click_cart_button() 

    #new web page means new object class
    cart_page = CartPage(logged_in)
    cart_page.click_checkout_button()

    #new web page
    checkout_page = CheckoutPage(logged_in)
    checkout_page.fill_checkout_details("abc","x","123")
    checkout_page.click_continue()

    #finish page
    finish_checkout = FinishCheckoutPage(logged_in)
    finish_checkout.click_finish()

    checkout_complete = CheckOutCompletePage(logged_in)
    expect (checkout_complete.checkout_header).to_have_text("Thank you for your order!")


def test_missing_fname(checkout):
    
    checkout_page = CheckoutPage(checkout)
    checkout_page.fill_checkout_details("","x","123")
    checkout_page.click_continue()

    expect (checkout_page.error_text).to_have_text("Error: First Name is required")



