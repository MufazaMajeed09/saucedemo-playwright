class FinishCheckoutPage:

    def __init__(self,page):
        self.finish_button = page.locator('[data-test="finish"]')

    def click_finish(self):
        self.finish_button.click()      
