import unittest
import HtmlTestRunner
import time
from selenium import webdriver
from PageObjects.Login import Login
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__  = "tudorache@gmail.com"


class LoginTest21(unittest.TestCase):
    driver = webdriver.Chrome()
    email_address = "sephoramajordome3500@gmail.com"
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

    def test_login_21(self):
        login = Login(self.driver)

        # Click "Sign In" link
        login.close_icon()
        login.click_signin()

        # Enter an invalid email
        login.set_email_address(self.email_address)

        # Click "Forgot?" link
        login.click_forgot_link()

        # Check if previously entered email is present in email field
        element = self.driver.find_elements_by_xpath(Login.check_invalid_forgot_email)
        if len(element) > 0:
            print("OK. Previously entered email is present in email field.")
        else:
            sys.exit("ERROR. Previously entered email is not present in email field.")

        # Click "Send Email" button
        login.click_send_email_button()
        time.sleep(1)

        # Check if there is an error message regarding the email
        element = self.driver.find_elements_by_xpath(Login.alert_send_email)
        if len(element) > 0:
            print("OK. An alert text message is present.")
        else:
            sys.exit("ERROR. No alert text message is present.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="LoginTest21"))
