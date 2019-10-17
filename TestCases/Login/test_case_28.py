import unittest
import HtmlTestRunner
import time
from selenium import webdriver
from PageObjects.Login import Login
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__  = "tudorache@gmail.com"


class LoginTest28(unittest.TestCase):
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

    def test_login_28(self):
        login = Login(self.driver)

        # Click "Sign In" link
        login.close_icon()
        login.click_signin()

        # Click "Privacy Policy" link
        login.click_privacy_policy()
        time.sleep(1)

        # Check if "Privacy Policy" page has oppened, if no => error
        element = self.driver.find_elements_by_xpath(Login.check_privacy_policy)
        if len(element) > 0:
            print("OK. The user can see Privacy Policy.")
        else:
            sys.exit("ERROR.  The user cannot see Privacy Policy.")

        # Click "X" in the right top corner
        login.click_close_privacy_policy()

        # Check if user returned to "Sign In" page
        element = self.driver.find_elements_by_xpath(Login.check_please_signin)
        if len(element) > 0:
            print("OK. User returned to Sign In page.")
        else:
            sys.exit("ERROR. User didn't return to Sign In page.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="LoginTest28"))
