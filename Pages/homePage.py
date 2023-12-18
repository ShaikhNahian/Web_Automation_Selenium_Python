from Locators.locators import Locators

class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.profile_dropdown_icon = Locators.profile_dropdown_icon
        self.logout_link = Locators.logout_link

    def click_profile_dropdown(self):
        self.driver.find_element(*self.profile_dropdown_icon).click()

    def click_logout(self):
        self.driver.find_element(*self.logout_link).click()
