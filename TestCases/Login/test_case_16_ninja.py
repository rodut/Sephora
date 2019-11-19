import unittest
import HtmlTestRunner
from selenium import webdriver
from PageObjects.LoginNinja import LoginNinja
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__  = "tudorache@gmail.com"


class LoginTest16Ninja(unittest.TestCase):
    driver = webdriver.Chrome()
    email_address = "jacknicholson@gmail.com"
    password = "1234567890"

    @classmethod
    def setUpClass(cls):
        cls.driver.maximize_window()
        login = LoginNinja(cls.driver)
        cls.driver.get(login.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_16_ninja(self):
        login = LoginNinja(self.driver)
        # Click "My Account" link
        login.click_my_account_link()
        # Click "Login" link
        login.click_login_link()
        # Enter valid email
        login.set_email(self.email_address)
        # Enter the old password
        login.set_password(self.password)
        # Click "Continue" button
        login.click_login_button()
        # Check if user is not login, if user logged in => error
        element = self.driver.find_element_by_xpath(LoginNinja.warning_message).is_displayed()
        assert element, "ERROR. User can login with his old password."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="LoginTest16Ninja"))
