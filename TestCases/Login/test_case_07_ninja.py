
import unittest
import HtmlTestRunner
from selenium import webdriver
from PageObjects.LoginNinja import LoginNinja
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class LoginTest07Ninja(unittest.TestCase):
    driver = webdriver.Chrome()
    email = "jacknicholson@gmail.com"
    password = "1234567890"

    @classmethod
    def setUpClass(cls):
        reg = LoginNinja(cls.driver)
        cls.driver.get(reg.url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_07_ninja(self):
        login = LoginNinja(self.driver)
        # Click on "My Account" link
        login.click_my_account_link()
        # Click on "Login" link
        login.click_login_link()
        # Enter a valid email in email field
        login.set_email(self.email)
        # Enter a invalid password in password field
        login.set_password(self.password)
        # Click on "Login" button
        login.click_login_button()
        # Verify if user cannot login with valid email/pass
        element = self.driver.find_element_by_xpath(LoginNinja.warning_message).is_displayed()
        assert element, "ERROR. User can login with invalid password."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="LoginTest07Ninja"))
