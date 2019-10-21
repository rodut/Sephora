import unittest
import HtmlTestRunner
import time
from selenium import webdriver
from PageObjects.Login import Login
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__  = "tudorache@gmail.com"


class LoginTest10(unittest.TestCase):
    driver = webdriver.Chrome()
    email_address = ""
    password = ""
    @classmethod
    def setUpClass(cls):
        login = Login(cls.driver)
        cls.driver.get(login.url)
        cls.driver.maximize_window()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_10(self):
        login = Login(self.driver)
        # Clicking "Sign In" link
        login.close_icon()
        login.click_signin()
        # Enter an empty email in email field
        login.set_email_address(self.email_address)
        # Enter an empty password in password field
        login.set_password(self.password)
        # Click on "Continue" button
        login.click_continue()
        # Verify if user cannot login with empty email and empty pass
        element = self.driver.find_elements_by_xpath(Login.alert_no_email_address)
        if len(element) > 0:
            print("OK. Missing email error text is present.")
        else:
            sys.exit("ERROR. Missing email error text is no present.")
        element = self.driver.find_elements_by_xpath(Login.alert_pass_missing)
        if len(element) > 0:
            print("OK. Missing password error text is present.")
        else:
            sys.exit("ERROR. password email error text is no present.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="LoginTest10"))
