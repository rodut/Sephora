import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.Register import Register
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"


class RegisterTest004(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        reg = Register(cls.driver)
        cls.driver.get(reg.url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_register_04(self):
        wait = WebDriverWait(self.driver, 10)
        reg = Register(self.driver)
        reg.close_icon()
        # Click "Register" link
        reg.click_register()
        # Click "Register" button
        reg.click_register_button()
        # Verify that system generates an error message when clicking on "REGISTER" button without filling all the mandatory fields
        element = wait.until(EC.presence_of_element_located((By.XPATH, Register.alert_msg_first_name)))
        assert element.is_displayed()
        element = self.driver.find_element_by_xpath(Register.alert_msg_last_name)
        assert element.is_displayed()
        element = self.driver.find_element_by_xpath(Register.alert_msg_email_address)
        assert element.is_displayed()
        element = self.driver.find_element_by_xpath(Register.alert_msg_password)
        assert element.is_displayed()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="RegisterTest04"))
