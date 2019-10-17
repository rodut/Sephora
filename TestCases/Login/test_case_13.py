import unittest
import HtmlTestRunner
import time
from PageObjects.Login import Login
from selenium import webdriver
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__  = "tudorache@gmail.com"


class LoginTest13(unittest.TestCase):
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

    def test_login_13(self):
        login = Login(self.driver)

        # Clicking "Sign In" link
        login.close_icon()
        login.click_signin()

        # Enter valid email
        login.set_email_address(self.email_address)

        # Enter valid password
        login.set_password(self.password)

        # Verify if the password is in encrypted form, of no => error
        element = self.driver.find_elements_by_xpath(Login.encrypted_password)
        if len(element) > 0:
            print("OK. Password is in encrypted form.")
        else:
            sys.exit("ERROR. Password is not in encrypted form.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="LoginTest13"))
