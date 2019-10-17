import unittest
import HtmlTestRunner
import time
from PageObjects.Login import Login
from selenium import webdriver
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__  = "tudorache@gmail.com"


class LoginTest08(unittest.TestCase):
    driver = webdriver.Chrome()
    email_address = ""
    password = "123456789"

    @classmethod
    def setUpClass(cls):
        login = Login(cls.driver)
        cls.driver.get(login.url)
        cls.driver.maximize_window()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_08(self):
        login = Login(self.driver)

        # Clicking "Sign In" link
        login.close_icon()
        login.click_signin()

        # Enter an empty email in email field
        login.set_email_address(self.email_address)

        # Enter a valid password in password field
        login.set_password(self.password)

        # Click on "Continue" button
        login.click_continue()

        # Verify if user cannot login with empty email address
        element = self.driver.find_elements_by_xpath(Login.alert_no_email_address)
        if len(element) > 0:
            print("OK. Missing email error text is present.")
        else:
            sys.exit("ERROR. Missing email error text is no present.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="LoginTest08"))
