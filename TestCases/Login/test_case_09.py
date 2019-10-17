import unittest
import HtmlTestRunner
from selenium import webdriver
import time
from PageObjects.Login import Login
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__  = "tudorache@gmail.com"


class LoginTest09(unittest.TestCase):
    driver = webdriver.Chrome()
    email_address = "sephoramajor@gmail.com"
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

    def test_login_09(self):
        login = Login(self.driver)
        login.close_icon()
        login.click_signin()
        login.set_email_address(self.email_address)
        login.set_password(self.password)
        login.click_continue()
        element = self.driver.find_elements_by_xpath(Login.alert_pass_missing)
        if len(element) > 0:
            print("OK. Missing password error text is present.")
        else:
            sys.exit("ERROR. password email error text is no present.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="LoginTest09"))
