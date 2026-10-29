class LoginPage:

    def __init__(self,page):
        self.page = page
        self.username = page.locator('[data-test="username"]')
        self.password = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')
        self.error_text = page.locator('[data-test="error"]')


    def open_login_page(self):
        self.page.goto("https://www.saucedemo.com/")  

    def enter_username(self, username):
        self.username.fill(username)   

    def enter_password(self, password):
        self.password.fill(password)         

    def  press_login(self):
        self.login_button.click()        
