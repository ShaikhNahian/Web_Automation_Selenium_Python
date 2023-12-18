from selenium import webdriver
import time
import unittest
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from Pages.homePage import HomePage
from Pages.loginPage import LoginPage
import HtmlTestRunner
class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(10)

    def test01_login_valid(self):
        driver = self.driver


        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()


        homepage = HomePage(driver)
        homepage.click_profile_dropdown()
        time.sleep(2)
        homepage.click_logout()

        time.sleep(2)

    def test02_login_invalid_username(self):
        driver = self.driver


        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Abba")
        login.enter_password("admin123")
        login.click_login()
        message = login.check_invalid_username_message()
        self.assertEqual(message, "Invalid Credentials420")

        time.sleep(2)

    def test03_login_invalid_pass(self):
        driver = self.driver


        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("ABBA")
        login.click_login()
        message = login.check_invalid_username_message()
        self.assertEqual(message, "Invalid Credentials420")

        time.sleep(2)

    def test04_login_invalid_creds(self):
        driver = self.driver


        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin11")
        login.enter_password("ABBA")
        login.click_login()
        message = login.check_invalid_username_message()
        self.assertEqual(message, "Invalid Credentials420")

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='E:/Projects/Selenium/SeleniumPython/Web_Automation_POM_UnitTest_HTMLReports/pythonProject1/Reports'))









