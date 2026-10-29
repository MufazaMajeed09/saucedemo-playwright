class CheckoutPage:

    def __init__ (self,page):
        self.fname = page.locator('[data-test="firstName"]')
        self.lname=page.locator('[data-test="lastName"]')
        self.code = page.locator('[data-test="postalCode"]')

        self.continue_button = page.locator('[data-test="continue"]')

    def fill_checkout_details(self,fname,lname,code):
        self.fname.fill(fname)
        self.lname.fill(lname)
        self.code.fill(code)

    def click_continue(self):
        self.continue_button.click()   