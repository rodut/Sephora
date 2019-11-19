import unittest
import HtmlTestRunner
from selenium import webdriver
from PageObjects.Register import Register
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"


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
        assert element, "ERROR. Password field type is not 'password', so the field is not encrypted by default."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="RegisterTest12"))
