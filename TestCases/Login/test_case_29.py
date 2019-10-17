import unittest
import HtmlTestRunner
import time
from selenium import webdriver
from PageObjects.Login import Login
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__  = "tudorache@gmail.com"


class LoginTest29(unittest.TestCase):
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

    def test_login_29(self):
        login = Login(self.driver)

        # Click "Sign In" link
        login.close_icon()
        login.click_signin()
        time.sleep(2)

        # 3. Click "Terms of Use" link
        login.click_terms_of_use()
        time.sleep(2)

        # Check if "Terms of Use" page has opened, if no => error
        element = self.driver.find_elements_by_xpath(Login.check_terms_of_use)
        if len(element) > 0:
            print("OK. The user can see Terms of Use.")
        else:
            sys.exit("ERROR.  The user cannot see Terms of Use.")

        # Click "X" in the right top corner
        login.click_close_terns_of_use()

        # Check if user returned to "Sign In" page
        element = self.driver.find_elements_by_xpath(Login.check_please_signin)
        if len(element) > 0:
            print("OK. User returned to Sign In page.")
        else:
            sys.exit("ERROR. User didn't return to Sign In page.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="LoginTest29"))
