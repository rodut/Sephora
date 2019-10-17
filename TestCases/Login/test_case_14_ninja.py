import unittest
import HtmlTestRunner
from selenium import webdriver
import time
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

        # Click "My Account" link
        login.click_my_account_link()

        # Click "Login" link
        login.click_login_link()

        # Enter valid email
        login.set_email(self.email_address)

        # Enter valid password
        login.set_password(self.password)

        # Copy password (ctrl+c), than delete password, than paste password (ctrl+v)
        login.verify_password()

        # Click "Login" button
        login.click_login_button()

        # An warning should appear: "No match for E-Mail Address and/or Password."
        element = self.driver.find_element_by_xpath(LoginNinja.warning_message).is_displayed()
        if element:
            print("OK. User cannot copy/paste the password with asterisks.")
        else:
            sys.exit("ERROR. User can copy/paste the password with asterisks.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="LoginTest14Ninja"))
