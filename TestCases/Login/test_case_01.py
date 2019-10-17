import unittest
import HtmlTestRunner
from selenium import webdriver
import time
from PageObjects.Login import Login
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__  = "tudorache@gmail.com"


class LoginTest01(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        login = Login(cls.driver)
        cls.driver.get(login.url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_00(self):
        login = Login(self.driver)

        # Clicking "Sign In" link
        login.close_icon()
        login.click_signin()

        # Verifying if the link "Sign In" was opened
        element = self.driver.find_elements_by_xpath(Login.yes_pass_selected)
        if len(element) > 0:
            print("OK. Radio button 'Yes, I have a password' is selected by default.")
        else:
            sys.exit("ERROR. Radio button 'Yes, I have a password' is not selected by default.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="LoginTest00"))
