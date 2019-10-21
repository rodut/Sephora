import unittest
from selenium import webdriver
import HtmlTestRunner
from PageObjects.Register import Register
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class RegisterTest008(unittest.TestCase):
    driver = webdriver.Chrome()
    first_name = "Jack"
    last_name = "Nicholson"
    email_address = "hhgfgfgfgf@gmailcom"
    password = "whatever"

    @classmethod
    def setUpClass(cls):
        reg = Register(cls.driver)
        cls.driver.get(reg.url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_register_08(self):
        reg = Register(self.driver)
        reg.close_icon()
        # Click on "Register" link
        reg.click_register()
        # Enter valid first name
        reg.set_first_name(self.first_name)
        # Enter valid last name
        reg.set_last_name(self.last_name)
        # Enter incorrect email address
        reg.set_email_address(self.email_address)
        # Enter valid password
        reg.set_password(self.password)
        # Click "REGISTER" button
        reg.click_register_button()
        # Verify that the validation of email field by entering incorrect email address
        element = self.driver.find_elements_by_xpath(Register.alert_incorrect_email)
        if len(element) > 0:
            print("OK. System generates a validation error message when entering incorrect email format.")
        else:
            sys.exit("Error. System doesn't generate a validation error message when entering incorrect email format.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="RegisterTest08"))
