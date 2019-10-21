import unittest
from selenium import webdriver
import HtmlTestRunner
from PageObjects.Register import Register
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class RegisterTest005(unittest.TestCase):
    driver = webdriver.Chrome()
    first_name = "        "
    last_name = "       "
    email_address = "       "
    password = "       "

    @classmethod
    def setUpClass(cls):
        reg = Register(cls.driver)
        cls.url = reg.url
        cls.driver.get(cls.url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_register_05(self):
        reg = Register(self.driver)
        reg.close_icon()
        # Click on "Register" link
        reg.click_register()
        # Enter "           " in the "First name" field
        reg.set_first_name(self.first_name)
        # Enter "           " in the "Last name" field
        reg.set_last_name(self.last_name)
        # Enter "           " in the "Email address" field
        reg.set_email_address(self.email_address)
        # Enter "           " in the "Password" field
        reg.set_password(self.password)
        # Click on "REGISTER" button
        reg.click_register_button()
        # Verify that entering blank spaces on mandatory fields lead to validation error message
        element = self.driver.find_elements_by_xpath(Register.alert_msg_first_name)
        if len(element) > 0:
            print("OK. Alert message for 'First Name' is present.")
        else:
            sys.exit("Error. Alert message for 'First Name' is not present.")
        element = self.driver.find_elements_by_xpath(Register.alert_msg_last_name)
        if len(element) > 0:
            print("OK. Alert message for 'Last Name' is present.")
        else:
            sys.exit("Error. Alert message for 'Last Name' is not present.")
        element = self.driver.find_elements_by_xpath(Register.alert_msg_email_address)
        if len(element) > 0:
            print("OK. Alert message for 'Email Address' is present.")
        else:
            sys.exit("Error. Alert message for 'Email Address' is not present.")
        element = self.driver.find_elements_by_xpath(Register.alert_msg_password)
        if len(element) > 0:
            print("OK. Alert message for 'Password' is present.")
        else:
            sys.exit("Error. Alert message for 'Password' is not present.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="RegisterTest05"))


