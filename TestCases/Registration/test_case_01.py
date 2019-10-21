__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"

import unittest
import HtmlTestRunner
from selenium import webdriver
from PageObjects.Register import Register
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")


class RegisterTest001(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        reg = Register(cls.driver)
        cls.driver.get(reg.url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_register_001(self):
        reg = Register(self.driver)
        reg.close_icon()
        # Click on "Register" link
        reg.click_register()
        # Check if Registration form contains the following field: first name, last name, email address, password, month, day, year, zip code
        element = self.driver.find_elements_by_xpath(Register.first_name_id)
        if len(element) > 0:
            print("OK. 'First Name' field is present.")
        else:
            sys.exit("Error. First Name field is not present.")

        element = self.driver.find_elements_by_xpath(Register.last_name_id)
        if len(element) > 0:
            print("OK. 'Last Name' field is present.")
        else:
            sys.exit("Error. 'Last Name' field is not present.")

        element = self.driver.find_elements_by_xpath(Register.email_address_id)
        if len(element) > 0:
            print("OK. 'Email Address' field if present.")
        else:
            sys.exit("Error. 'Email Address' field is not present.")

        element = self.driver.find_elements_by_xpath(Register.password_id)
        if len(element) > 0:
            print("OK. 'Password' field is present.")
        else:
            sys.exit("Error. 'Password' field is not present.")

        element = self.driver.find_elements_by_xpath(Register.month_id)
        if len(element) > 0:
            print("OK. Drop-down list 'Month' is present.")
        else:
            sys.exit("Error. Drop-down list 'Month' is not present.")

        element = self.driver.find_elements_by_xpath(Register.day_id)
        if len(element) > 0:
            print("OK. Drop-down list 'Day' is present.")
        else:
            sys.exit("Error. Drop-down list 'Day' is not present.")

        element = self.driver.find_elements_by_xpath(Register.year_id)
        if len(element) > 0:
            print("OK. Drop-down list 'Year' is present.")
        else:
            sys.exit("Error. Drop-down list 'Year' is not present.")

        element = self.driver.find_elements_by_xpath(Register.zip_id)
        if len(element) > 0:
            print("OK. 'ZIP Code' field is present.")
        else:
            sys.exit("Error. 'ZIP Code' field is not present.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="RegisterTest001"))
