
from playwright.sync_api import expect, Page
import pytest

def test_six_products(logged_in):

    expect(logged_in.locator('[data-test="inventory-item"]')).to_have_count(6)


def test_price_lo_to_high(logged_in):
    
    logged_in.locator('[data-test="product-sort-container"]').select_option("lohi")
    list_of_items =[]
    copy_list_of_items = [] 
    processed_list=[]

    list_of_items=(logged_in.locator('[data-test="inventory-item-price"]')).all_inner_texts()
     
    for item in list_of_items:
        a=item.replace("$", "")
        b=float(a)
        processed_list.append(b)

    copy_list_of_items = processed_list.copy()
    processed_list.sort()
    assert processed_list==copy_list_of_items

