import unittest
import time
import HtmlTestRunner
from selenium import webdriver
from PageObjects.Register import Register
import sys

sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class RegisterTest016(unittest.TestCase):
    driver = webdriver.Chrome()
    first_name = "Jacky"
    last_name = "Nicholsons"
    email_address = "trulala@jojo.com"
    password = "123456789"

    @classmethod
    def setUpClass(cls):
        reg = Register(cls.driver)
        cls.driver.get(reg.url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_register_16(self):
        reg = Register(self.driver)
        reg.close_icon()
        # Click on "Register" link
        reg.click_register()
        # Enter data in all the mandatory fields
        reg.set_first_name(self.first_name)
        reg.set_last_name(self.last_name)
        reg.set_email_address(self.email_address)
        reg.set_password(self.password)
        # Click on "Yes, join Sephora’s free rewards program and earn points on every purchase" checkbox
        reg.click_yes_join_sephora()
        # Verify if "Subscribe to Sephora emails" is not clickable
        element = self.driver.find_element_by_xpath(reg.subscribe_emails_disabled)
        assert element, "ERROR. Checkbox is clickable."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="RegisterTest16"))
