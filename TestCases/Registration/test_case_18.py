import unittest
import time
import HtmlTestRunner
from selenium import webdriver
from PageObjects.Register import Register
import sys

sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class RegisterTest018(unittest.TestCase):
    driver = webdriver.Chrome()
    first_name = "Jacky"
    last_name = "Nicholsons"
    email_address = "trulala@jojo.com"
    password = "123456789"
    zip_code = "AB1234"

    @classmethod
    def setUpClass(cls):
        reg = Register(cls.driver)
        cls.driver.get(reg.url)
        cls.driver.maximize_window()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_register_018(self):
        reg = Register(self.driver)
        reg.close_icon()
        # Click on "Register" link
        reg.click_register()
        # Complete all the mandatory fields
        reg.set_first_name(self.first_name)
        reg.set_last_name(self.last_name)
        reg.set_email_address(self.email_address)
        reg.set_password(self.password)
        # Enter a incorrect zip code (ex. AB6585)
        reg.set_zip_code(self.zip_code)
        # Click "REGISTER" button
        reg.click_register_button()
        # Check if an error message appears
        element = self.driver.find_elements_by_xpath(reg.alert_zip_code)
        if len(element) > 0:
            print("OK. Alert message is visible.")
        else:
            sys.exit("ERROR. Alert message is not visible.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="RegisterTest018"))
