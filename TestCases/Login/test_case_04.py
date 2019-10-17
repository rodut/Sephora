import unittest
import HtmlTestRunner
import time
from PageObjects.Login import Login
from selenium import webdriver
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__  = "tudorache@gmail.com"


class LoginTest04(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        login = Login(cls.driver)
        cls.driver.get(login.url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_04(self):
        login = Login(self.driver)

        # Clicking "Sign In" link
        login.close_icon()
        login.click_signin()

        # Verifying if 'Continue' button is present.
        element = self.driver.find_elements_by_xpath(Login.continue_button)
        if len(element) > 0:
            print("OK. 'Continue' button is present.")
        else:
            sys.exit("ERROR. 'Continue' button is not present.")

        # Verifying if 'Terms of Use' link is present.
        element = self.driver.find_elements_by_xpath(Login.terms_of_use_link)
        if len(element) > 0:
            print("OK. 'Terms of Use' link is present.")
        else:
            sys.exit("ERROR. 'Terms of Use' link is not present.")

        # Verifying if 'Privacy Policy' link is present.
        element = self.driver.find_elements_by_xpath(Login.privacy_policy_link)
        if len(element) > 0:
            print("OK. 'Privacy Policy' link is present.")
        else:
            sys.exit("ERROR. 'Privacy Policy' link is present.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="LoginTest04"))
