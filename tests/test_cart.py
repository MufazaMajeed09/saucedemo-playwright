from playwright.sync_api import expect, Page
import pytest

def test_add_to_cart_shows_badge(logged_in):
    logged_in.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    expect (logged_in.locator('[data-test="shopping-cart-badge"]')).to_have_text(str(1))

def test_remove_from_cart_hides_badge(logged_in):
   logged_in.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
   logged_in.locator('[data-test="remove-sauce-labs-backpack"]').click()
   expect (logged_in.locator('[data-test="shopping-cart-badge"]')).to_be_hidden()