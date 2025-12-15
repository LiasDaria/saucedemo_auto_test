class LoginPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, page):
        self.page = page
        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"
        self.error_message = "h3[data-test='error']"

    def open(self):
        self.page.goto(self.URL)

    def login(self, username, password):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def get_error_text(self):
        if self.page.is_visible(self.error_message):
            return self.page.inner_text(self.error_message)
        return ""