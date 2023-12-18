from selenium.webdriver.common.by import By


class Locators:

    #login page objects
    username_textbox = (By.NAME, "username")
    password_textbox = (By.NAME, "password")
    login_button = (By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
    invalidUsername_message = (By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p")

    #Homepage objects
    profile_dropdown_icon = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/i")
    logout_link = (By.LINK_TEXT, "Logout")
