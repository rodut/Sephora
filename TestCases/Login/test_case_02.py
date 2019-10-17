import unittest
import HtmlTestRunner
from selenium import webdriver
from PageObjects.Login import Login
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__  = "tudorache@gmail.com"


class LoginTest02(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        login = Login(cls.driver)
        cls.driver.get(login.url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_01(self):
        login = Login(self.driver)

        # Clicking "Sign In" link
        login.close_icon()
        login.click_signin()

        # Verifying if 'Email address' field is present.
        element = self.driver.find_elements_by_xpath(Login.email_address_id)
        if len(element) > 0:
            print("OK. 'Email address' field is present.")
        else:
            sys.exit("ERROR. 'Email address' field is not present.")

        # Verifying if 'No, I am new to the website' radio button is present.
        element = self.driver.find_elements_by_xpath(Login.no_password)
        if len(element) > 0:
            print("OK. 'No, I am new to the website' radio button is present.")
        else:
            sys.exit("ERROR. 'No, I am new to the website' radio button is not present.")

        # Verifying if 'Yes, I have a password' radio button is present.
        element = self.driver.find_elements_by_xpath(Login.yes_password)
        if len(element) > 0:
            print("OK. 'Yes, I have a password' radio button is present.")
        else:
            sys.exit("ERROR. 'Yes, I have a password' radio button is not present.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="LoginTest01"))
