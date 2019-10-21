import unittest
import HtmlTestRunner
from selenium import webdriver
from PageObjects.Register import Register
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class RegisterTest012(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        reg = Register(cls.driver)
        cls.driver.get(reg.url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_register_12(self):
        reg = Register(self.driver)
        reg.close_icon()
        # Click on "Register" link
        reg.click_register()
        # Verify that the password is in encrypted form when entered
        element = self.driver.find_element_by_xpath(Register.password_type).is_displayed()
        if element:
            print("OK. Password field type is 'password', so the field is encrypted by default.")
        else:
            sys.exit("ERROR. Password field type is not 'password', so the field is not encrypted by default.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="RegisterTest12"))
