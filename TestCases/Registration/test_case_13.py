import unittest
import HtmlTestRunner
from selenium import webdriver
from PageObjects.Register import Register
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class RegisterTest013(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        reg = Register(cls.driver)
        cls.driver.get(reg.url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_register_13(self):
        reg = Register(self.driver)
        reg.close_icon()
        # Click on "Register" link
        reg.click_register()
        # Click "Terms & Conditions" link
        reg.click_terms_conditions()
        # Verify if "Terms & Conditions" link was opened
        element = self.driver.find_element_by_xpath(Register.terms_conditions_verification).is_displayed()
        if element:
            print("OK. User can see 'Terms & Conditions' page.")
        else:
            sys.exit("ERROR. User cannot see 'Terms & Conditions' page.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="RegisterTest13"))
