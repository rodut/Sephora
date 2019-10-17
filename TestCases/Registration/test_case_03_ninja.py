import unittest
import HtmlTestRunner
import time
from selenium import webdriver
from PageObjects.RegisterNinja import RegisterNinja
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class RegisterTest003(unittest.TestCase):
    driver = webdriver.Chrome()
    first_name = "Jack"
    last_name = "Nicholson"
    email = "jacknicholson@gmail.com"
    telephone = "12122256998"
    password = "123456789"
    password_confirm = "123456789"

    @classmethod
    def setUpClass(cls):
        reg = RegisterNinja(cls.driver)
        cls.driver.get(reg.url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_register_003_ninja(self):
        reg = RegisterNinja(self.driver)
        reg.click_my_account_link()
        reg.click_register_link()
        reg.set_first_name(self.first_name)
        reg.set_last_name(self.last_name)
        reg.set_email(self.email)
        reg.set_telephone(self.telephone)
        reg.set_password(self.password)
        reg.set_password_confirm(self.password_confirm)
        reg.click_privacy_policy_checkbox()
        reg.click_continue_button()
        time.sleep(1)
        element = self.driver.find_element_by_xpath(RegisterNinja.success_link).is_displayed()
        if element:
            print("OK. 'Success' link is visible, so user made an account.")
        else:
            sys.exit("ERROR. 'Success' link is invisible, there is a problem with creating an account.")
        reg.click_continue_button_2()
        element = self.driver.find_element_by_xpath(RegisterNinja.account_link).is_displayed()
        if element:
            print("OK. User had been logged in.")
        else:
            sys.exit("ERROR. There is a problem with login process.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="RegisterTest003"))
