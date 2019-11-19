import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import HtmlTestRunner
from selenium import webdriver
from PageObjects.Register import Register
import sys

sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"


class RegisterTest018(unittest.TestCase):
    driver = webdriver.Chrome()
    first_name = "Jacky"
    last_name = "Nicholsons"
    email_address = "trulala@jojo.com"
    password = "123456789"
    zip_code = "AB1234554"

    @classmethod
    def setUpClass(cls):
        reg = Register(cls.driver)
        cls.driver.get(reg.url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_register_018(self):
        wait = WebDriverWait(self.driver, 10)
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
        element = wait.until(EC.presence_of_element_located((By.XPATH, reg.alert_zip_code)))
        assert element.is_displayed(), "ERROR. Alert message is not visible."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="RegisterTest018"))
