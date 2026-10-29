
class CartPage:

    def __init__(self,page):
        self.checkout_button=page.locator('[data-test="checkout"]')

    def click_checkout_button(self):
        self.checkout_button.click()    