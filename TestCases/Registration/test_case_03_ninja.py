import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.RegisterNinja import RegisterNinja
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"


class RegisterTest003(unittest.TestCase):
    driver = webdriver.Chrome()
    first_name = "Jack"
    last_name = "Nicholson"
    email = "jacknicholsonsss@gmail.com"
    telephone = "12122256998"
    password = "123456789"
    password_confirm = "123456789"

    @classmethod
    def setUpClass(cls):
        reg = RegisterNinja(cls.driver)
        cls.driver.get(reg.url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_register_03_ninja(self):
        wait = WebDriverWait(self.driver, 10)
        reg = RegisterNinja(self.driver)
        # Click on "My Account" link
        reg.click_my_account_link()
        # Click on "Register" link
        reg.click_register_link()
        # Compete the all mandatory fields
        reg.set_first_name(self.first_name)
        reg.set_last_name(self.last_name)
        reg.set_email(self.email)
        reg.set_telephone(self.telephone)
        reg.set_password(self.password)
        reg.set_password_confirm(self.password_confirm)
        # Click privacy policy checkbox
        reg.click_privacy_policy_checkbox()
        # Click "Continue" button
        reg.click_continue_button()
        # Verify that clicking on "Continue" button after entering all the mandatory fields, submits the data to the server
        element = wait.until(EC.presence_of_element_located((By.XPATH, RegisterNinja.success_link)))
        assert element.is_displayed()
        # Click on "Continue" button
        reg.click_continue_button_2()
        element = self.driver.find_element_by_xpath(RegisterNinja.account_link).is_displayed()
        assert element, "ERROR. There is a problem with login process."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="RegisterTest03"))
