from Locators.locators import Locators

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox = Locators.username_textbox
        self.password_textbox = Locators.password_textbox
        self.login_button = Locators.login_button
        self.invalidUsername_message = Locators.invalidUsername_message

    def enter_username(self, username):
        self.driver.find_element(*self.username_textbox).clear()
        self.driver.find_element(*self.username_textbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).clear()
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def check_invalid_username_message(self):
        msg = self.driver.find_element(*self.invalidUsername_message).text
        return msg





