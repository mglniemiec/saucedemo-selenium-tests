class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"
        self.username_input = "user-name"
        self.password_input = "password"
        self.login_button = "login-button"
        self.error_message_container = "error-message-container"

    def load(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.driver.find_element("id", self.username_input).send_keys(username)
        self.driver.find_element("id", self.password_input).send_keys(password)
        self.driver.find_element("id", self.login_button).click()

    def get_error_message(self):
        return self.driver.find_element("class name", self.error_message_container).text