__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"

import unittest
import HtmlTestRunner
import time
from selenium import webdriver
from PageObjects.Register import Register
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")


class RegisterTest003(unittest.TestCase):
    driver = webdriver.Chrome()
    first_name = "Jack"
    last_name = "Nicholson"
    email_address = "sephoramajor556@gmail.com"
    password = "whatever111"

    @classmethod
    def setUpClass(cls):
        reg = Register(cls.driver)
        cls.driver.get(reg.url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_register_03(self):
        reg = Register(self.driver)
        reg.close_icon()
        # Click on "Register" link
        reg.click_register()
        # Compete the all mandatory fields
        reg.set_first_name(self.first_name)
        reg.set_last_name(self.last_name)
        reg.set_email_address(self.email_address)
        reg.set_password(self.password)
        # Click "Continue" button
        reg.click_register_button()
        time.sleep(20)
        # Verify that clicking on "Continue" button after entering all the mandatory fields, submits the data to the server
        element = self.driver.find_elements_by_xpath("//*[@data-at='register']")
        if len(element) == 0:
            print("OK. User created a new profile.")
        else:
            sys.exit("Error. User didn't create a new profile.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="RegisterTest03"))
