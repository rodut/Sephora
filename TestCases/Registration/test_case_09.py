import unittest
from selenium import webdriver
import HtmlTestRunner
from PageObjects.Register import Register
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class RegisterTest009(unittest.TestCase):
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
        reg.click_register()
        reg.set_password(self.password)
        reg.click_register_eye_icon()
        element = self.driver.find_elements_by_xpath(Register.password_text)
        if len(element) > 0:
            print("OK. User can view his password as text.")
        else:
            sys.exit("Error. user cannot view his password as text.")
        reg.click_register_eye_icon()
        element = self.driver.find_elements_by_xpath(Register.password_asterisks)
        if len(element) > 0:
            print("OK. User can view his password as asterisks.")
        else:
            sys.exit("Error. User cannot view his password by asterisks.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="RegisterTest009"))
