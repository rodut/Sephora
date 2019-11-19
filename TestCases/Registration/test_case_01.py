__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"

import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
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
        wait = WebDriverWait(self.driver, 10)
        reg = Register(self.driver)
        reg.close_icon()
        # Click on "Register" link
        reg.click_register()
        # Check if Registration form contains the following field: first name, last name, email address, password, month, day, year, zip code
        element = wait.until(EC.presence_of_element_located((By.XPATH, Register.first_name_id)))
        assert element.is_displayed()
        element = self.driver.find_element_by_xpath(Register.last_name_id)
        assert element.is_displayed()
        element = self.driver.find_element_by_xpath(Register.email_address_id)
        assert element.is_displayed()
        element = self.driver.find_element_by_xpath(Register.password_id)
        assert element.is_displayed()
        element = self.driver.find_element_by_xpath(Register.month_id)
        assert element.is_displayed()
        element = self.driver.find_element_by_xpath(Register.day_id)
        assert element.is_displayed()
        element = self.driver.find_element_by_xpath(Register.year_id)
        assert element.is_displayed()
        element = self.driver.find_element_by_xpath(Register.zip_id)
        assert element.is_displayed()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="RegisterTest001"))
