import unittest
import HtmlTestRunner
import time
from PageObjects.Login import Login
from selenium import webdriver
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__  = "tudorache@gmail.com"


class LoginTest06(unittest.TestCase):
    driver = webdriver.Chrome()
    email_address = "abra@cadabra."
    password = "123456"

    @classmethod
    def setUpClass(cls):
        login = Login(cls.driver)
        cls.driver.get(login.url)
        cls.driver.maximize_window()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_06(self):
        login = Login(self.driver)
        # Clicking "Sign In" link
        login.close_icon()
        login.click_signin()
        # Enter a invalid email in email field
        login.set_email_address(self.email_address)
        # Enter a invalid password in password field
        login.set_password(self.password)
        # Click 'Continue' button
        login.click_continue()
        # Verify if alert email error text is present.
        element = self.driver.find_elements_by_xpath(Login.alert_incorrect_email)
        if len(element) > 0:
            print("OK. Alert email error text is present.")
        else:
            sys.exit("ERROR. Alert email error text is no present.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="LoginTest06"))
