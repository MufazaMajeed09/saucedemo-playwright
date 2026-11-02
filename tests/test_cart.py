from playwright.sync_api import expect, Page
import pytest
from pages.products_page import ProductsPage

def test_add_to_cart_shows_badge(logged_in):
    products_page = ProductsPage(logged_in)

    products_page.add_bag_pack()
    expect (products_page.car_badge).to_have_text(str(1))

def test_remove_from_cart_hides_badge(logged_in):
   products_page = ProductsPage(logged_in)
   products_page.add_bag_pack()
   products_page.remove_bag_pack()
   expect (products_page.car_badge).to_be_hidden()