
from playwright.sync_api import expect, Page
from pages.products_page import ProductsPage


def test_six_products(logged_in):
    products_page = ProductsPage(logged_in)
    expect(products_page.inventory_items).to_have_count(6)


def test_price_lo_to_high(logged_in):
    
    products_page = ProductsPage(logged_in)
    products_page.select_option_from_filter("lohi")
    list_of_items =[]
    copy_list_of_items = [] 
    processed_list=[]
    

    list_of_items=products_page.get_list_of_items()
    processed_list=products_page.process_list(list_of_items)
     

    copy_list_of_items = processed_list.copy()
    processed_list.sort()
    assert processed_list==copy_list_of_items

def test_price_high_to_low(logged_in):
    
    products_page = ProductsPage(logged_in)
    products_page.select_option_from_filter("hilo")
    list_of_items =[]
    copy_list_of_items = [] 
    processed_list=[]
    

    list_of_items=products_page.get_list_of_items()
    processed_list=products_page.process_list(list_of_items)
     

    copy_list_of_items = processed_list.copy()
    processed_list.sort(reverse=True)
    assert processed_list==copy_list_of_items

