import unittest
import HtmlTestRunner
import time
from PageObjects.Login import Login
from selenium import webdriver
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__  = "tudorache@gmail.com"


class LoginTest03(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        login = Login(cls.driver)
        cls.driver.get(login.url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_03(self):
        login = Login(self.driver)
        login.close_icon()
        login.click_signin()
        element = self.driver.find_elements_by_xpath(Login.password_field)
        if len(element) > 0:
            print("OK. 'Password' field is present.")
        else:
            sys.exit("ERROR. 'Password' field is not present.")
        element = self.driver.find_elements_by_xpath(Login.forgot_link)
        if len(element) > 0:
            print("OK. 'Forgot?' link is present.")
        else:
            sys.exit("ERROR. 'Forgot?' link is not present.")
        element = self.driver.find_elements_by_xpath(Login.cancel_button)
        if len(element) > 0:
            print("OK. 'Cancel' button is present.")
        else:
            sys.exit("ERROR. 'Cancel' button is not present.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="LoginTest03"))
