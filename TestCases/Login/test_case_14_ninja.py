import unittest
import HtmlTestRunner
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from PageObjects.LoginNinja import LoginNinja
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__  = "tudorache@gmail.com"


class LoginTest14Ninja(unittest.TestCase):
    driver = webdriver.Chrome()
    email_address = "jacknicholson@gmail.com"
    password = "123456789"

    @classmethod
    def setUpClass(cls):
        cls.driver.maximize_window()
        login = LoginNinja(cls.driver)
        cls.driver.get(login.url)
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_14_ninja(self):
        login = LoginNinja(self.driver)
        login.click_my_account_link()
        login.click_login_link()
        login.set_email(self.email_address)
        login.set_password(self.password)
        login.verify_password()
        login.click_login_button()
        element = self.driver.find_element_by_xpath(LoginNinja.warning_message).is_displayed()
        if element:
            print("OK. User cannot copy/paste the password with asterisks.")
        else:
            sys.exit("ERROR. User can copy/paste the password with asterisks.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="LoginTest14Ninja"))
