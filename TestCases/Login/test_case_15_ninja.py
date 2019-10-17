import unittest
import HtmlTestRunner
from selenium import webdriver
import time
from PageObjects.LoginNinja import LoginNinja
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__  = "tudorache@gmail.com"


class LoginTest15Ninja(unittest.TestCase):
    driver = webdriver.Chrome()
    email_address = "jacknicholson@gmail.com"
    password = "123456789"
    new_password = "1234567890"
    password_confirm = "1234567890"
    old_password = "123456789"
    old_pass_confirm = "123456789"

    @classmethod
    def setUpClass(cls):
        cls.driver.maximize_window()
        login = LoginNinja(cls.driver)
        cls.driver.get(login.url)
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_15_ninja(self):
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
        time.sleep(1)

        # Click "Password" link
        login.click_password_link()

        # Enter new password
        login.set_new_password(self.new_password)

        # Confirm new password
        login.set_password_confirm(self.password_confirm)

        # Click "Continue" button
        login.click_login_button()

        # User is logging out
        login.click_logout()

        # User is logging in the second time with the same e-mail and with the new password
        login.click_my_account_link()
        login.click_login_link()
        login.set_email(self.email_address)
        login.set_new_password(self.new_password)
        login.click_login_button()

        # User is changing the new password to the old one (It's vital to change the pass to initial one, because the next test cases are using the initial password)
        login.click_password_link()
        login.set_new_password(self.old_password)
        login.set_password_confirm(self.old_pass_confirm)
        login.click_login_button()

        # User is logging out
        login.click_my_account_link()
        login.click_logout()

        # User is logging in to verify if the password was changed to the initial one
        login.click_my_account_link()
        login.click_login_link()
        login.set_email(self.email_address)
        login.set_password(self.password)
        login.click_login_button()

        # Check if user signed in with the new password, if not => error
        element = self.driver.find_element_by_xpath(LoginNinja.logout_link).is_displayed()
        if element:
            print("OK. User changed his password successfully two times.")
        else:
            sys.exit("ERROR. User didn't change his password successfully.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="LoginTest15Ninja"))
