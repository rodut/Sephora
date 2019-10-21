import unittest
import HtmlTestRunner
import time
from selenium import webdriver
from PageObjects.LoginNinja import LoginNinja
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class LoginTest11Ninja(unittest.TestCase):
    driver = webdriver.Chrome()
    email_address = "jacknicholson@gmail.com"
    password = "123456789"

    @classmethod
    def setUpClass(cls):
        login = LoginNinja(cls.driver)
        cls.driver.get(login.url)
        cls.driver.maximize_window()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_11_ninja(self):
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
        # Click "Back Arrow" on browser button (2 times)
        login.windows_back_page()
        time.sleep(1)
        login.windows_back_page()
        time.sleep(1)
        # Click "My Account" link
        login.click_my_account_link()
        time.sleep(1)
        # Click "Login" link
        login.click_login_link()
        # Check if user is logged in, if not -> error (check if Logout link is present)
        element = self.driver.find_element_by_xpath(LoginNinja.logout_link)
        if element:
            print("OK. The user wasn't logged out.")
        else:
            sys.exit("ERROR. The user was logged out.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="LoginTest11Ninja"))
