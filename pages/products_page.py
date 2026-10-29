class ProductsPage:

    def __init__ (self,page):
        self.page = page
        self.inventory_items = page.locator('[data-test="inventory-item"]')
        self.sort_container = page.locator('[data-test="product-sort-container"]')
        self.item_price = page.locator('[data-test="inventory-item-price"]')


        self.add_bag_pack_item = page.locator('[data-test="add-to-cart-sauce-labs-backpack"]')
        self.car_badge = page.locator('[data-test="shopping-cart-badge"]')
        self.remove_bag_pack_item = page.locator('[data-test="remove-sauce-labs-backpack"]')

        self.cart_button = page.locator('[data-test="shopping-cart-link"]')
        
        
      


    def select_option_from_filter(self,option):
        self.sort_container.select_option(option) 

    def get_list_of_items(self):
        items_list = self.item_price.all_inner_texts()  
        return items_list   

    def process_list(self,list_of_items):
        processed_list=[]
        for item in list_of_items:
            a=item.replace("$", "")
            b=float(a)
            processed_list.append(b)
        return processed_list

    def add_bag_pack(self):
        self.add_bag_pack_item.click()

    def remove_bag_pack(self):
        self.remove_bag_pack_item.click()   

    def click_cart_button(self):
        self.cart_button.click() 













