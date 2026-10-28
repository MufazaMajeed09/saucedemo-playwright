from playwright.sync_api import expect, Page
import pytest

def test_check_out(logged_in):
    logged_in.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    logged_in.locator('[data-test="shopping-cart-link"]').click()
    logged_in.locator('[data-test="checkout"]').click()
    logged_in.locator('[data-test="firstName"]').fill("abc")
    logged_in.locator('[data-test="lastName"]').fill("abc")
    logged_in.locator('[data-test="postalCode"]').fill("abc")
    logged_in.locator('[data-test="continue"]').click()
    logged_in.locator('[data-test="finish"]').click()
    expect (logged_in.locator('[data-test="complete-header"]')).to_have_text("Thank you for your order!")

