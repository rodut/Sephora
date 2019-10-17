import unittest
import HtmlTestRunner
import time
from selenium import webdriver
from PageObjects.LoginNinja import LoginNinja
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__  = "tudorache@gmail.com"


class LoginTest22Ninja(unittest.TestCase):
    driver = webdriver.Chrome()
    email_address = "jacknicholson@gmail.com"

    @classmethod
    def setUpClass(cls):
        cls.driver.maximize_window()
        login = LoginNinja(cls.driver)
        cls.driver.get(login.url)
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_22_ninja(self):
        login = LoginNinja(self.driver)

        # Click "My Account" link
        login.click_my_account_link()

        # Click "Login" link
        login.click_login_link()

        # Click "Forgotten Password" link
        login.click_forgotten_password_link()

        # Enter a valid email
        login.set_email(self.email_address)

        # Click "Continue" button
        login.click_login_button()

        # Check if a confirmation message appeared
        element = self.driver.find_element_by_xpath(LoginNinja.confirm_message).is_displayed()
        if element:
            print("OK. An email with a confirmation link has been sent to the user's email address.")
        else:
            sys.exit("ERROR. An email with a confirmation link was not sent to the user's email address.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="LoginTest22Ninja"))
