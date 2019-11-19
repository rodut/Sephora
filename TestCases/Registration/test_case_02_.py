__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"

# '"*"'

import unittest
import HtmlTestRunner
from selenium import webdriver
from PageObjects.Register import Register
import time
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")


class RegisterTest002(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        reg = Register(cls.driver)
        cls.driver.get(reg.url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_register_02(self):
        reg = Register(self.driver)
        reg.close_icon()
        # Click on "Register" link
        reg.click_register()
        # Verify if all the required/mandatory fields are marked with *
        xpath = "//*[@for='firstName']"
        element = self.driver.execute_script("return window.getComputedStyle(document.querySelector('.css-1tuyf6g'),':after').getPropertyValue('content')")
        assert element in xpath, "Error. the field doesn't have asterisk, so it's not a mandatory field."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="RegisterTest02"))

