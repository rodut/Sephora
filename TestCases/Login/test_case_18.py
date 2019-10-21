import unittest
import HtmlTestRunner
import time
from selenium import webdriver
from PageObjects.Login import Login
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__  = "tudorache@gmail.com"


class LoginTest18(unittest.TestCase):
    driver = webdriver.Chrome()
    email_address = "sephoramajordome11@gmail.com"
    password = "antibacterie"
    @classmethod
    def setUpClass(cls):
        login = Login(cls.driver)
        cls.driver.get(login.url)
        cls.driver.maximize_window()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_18(self):
        login = Login(self.driver)
        # Click "Sign In" link
        login.close_icon()
        login.click_signin()
        # Enter an unregistered email
        login.set_email_address(self.email_address)
        # Select "No, I am new to the website"
        login.click_new_to_site()
        # Click "Continue" button
        login.click_continue()
        time.sleep(1)
        # Check if a registration form appeared, if no => error
        element = self.driver.find_elements_by_xpath(Login.register_sephora)
        if len(element) > 0:
            print("OK. 'Register with Sephora' registration form appeared.")
        else:
            sys.exit("ERROR. 'Register with Sephora' registration form doesn't appear.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="LoginTest18"))
