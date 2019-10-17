import unittest
import HtmlTestRunner
import time
from selenium import webdriver
from PageObjects.LoginNinja import LoginNinja
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__  = "tudorache@gmail.com"


class LoginTest19Ninja(unittest.TestCase):
    driver = webdriver.Chrome()
    email_address = "jacknicholson@gmail.com"
    password = "1234567890"

    @classmethod
    def setUpClass(cls):
        cls.driver.maximize_window()
        login = LoginNinja(cls.driver)
        cls.driver.get(login.url)
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_19_ninja(self):
        login = LoginNinja(self.driver)

        # Click "My Account" link
        login.click_my_account_link()

        # Click "Login" link
        login.click_login_link()

        # Enter valid email
        login.set_email(self.email_address)

        # Enter valid password
        login.set_password(self.password)

        # Click "Login" button
        login.click_login_button()

        # Click "My Account" link
        login.click_my_account_link()

        # Click "Logout" link
        login.click_logout()

        # Check if user was signed out, if not => error
        element = self.driver.find_element_by_xpath(LoginNinja.check_sign_out).is_displayed()
        if element:
            print("OK. The user successfully signed out.")
        else:
            sys.exit("ERROR. The user didn't sign out.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="LoginTest19Ninja"))
