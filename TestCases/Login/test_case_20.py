import unittest
import HtmlTestRunner
import time
from selenium import webdriver
from PageObjects.Login import Login
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__  = "tudorache@gmail.com"


class LoginTest20(unittest.TestCase):
    driver = webdriver.Chrome()
    email_address = "sephoramajor@gmail.com"
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

    def test_login_20(self):
        login = Login(self.driver)
        login.close_icon()
        login.click_signin()
        login.set_email_address(self.email_address)
        login.click_forgot_link()
        time.sleep(1)
        element = self.driver.find_elements_by_xpath(Login.check_forgot_email)
        if len(element) > 0:
            print("OK. Previously entered email is present in email field.")
        else:
            sys.exit("ERROR. Previously entered email is not present in email field.")
        login.click_send_email_button()
        element = self.driver.find_elements_by_xpath(Login.reset_password)
        if len(element) > 0:
            print("OK. A message with 'Reset Password' is present")
        else:
            sys.exit("ERROR. There is no message with 'Reset Password' present")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="LoginTest20"))
