import unittest
from selenium import webdriver
import HtmlTestRunner
from PageObjects.Register import Register
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class RegisterTest09(unittest.TestCase):
    driver = webdriver.Chrome()
    password = "abracadabra"

    @classmethod
    def setUpClass(cls):
        reg = Register(cls.driver)
        cls.driver.get(reg.url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_register_009(self):
        reg = Register(self.driver)
        reg.close_icon()
        # Click on "Register" link
        reg.click_register()
        # Enter a valid password
        reg.set_password(self.password)
        # Click on "eye" icon
        reg.click_register_eye_icon()
        # Verify if clicking on "eye" icon will show the password
        element = self.driver.find_elements_by_xpath(Register.password_text)
        assert element, "Error. user cannot read his password as text."
        # Click on "eye" icon the second time
        reg.click_register_eye_icon()
        # Verify is clicking the second time will hide the password
        element = self.driver.find_elements_by_xpath(Register.password_asterisks)
        assert element, "Error. User read view his password."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="RegisterTest09"))
