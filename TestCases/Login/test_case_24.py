import unittest
import HtmlTestRunner
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from PageObjects.Login import Login
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__  = "tudorache@gmail.com"


class LoginTest24(unittest.TestCase):
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

    def test_login_24(self):
        login = Login(self.driver)
        login.close_icon()
        login.click_signin()
        login.close_icon()
        element = self.driver.find_elements_by_xpath(Login.check_please_signin)
        if len(element) > 0:
            sys.exit("ERROR. User didn't return to the main page.")
        else:
            print("OK. User returned to the main page.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="LoginTest24"))
