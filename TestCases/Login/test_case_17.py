import unittest
import HtmlTestRunner
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from PageObjects.Login import Login
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"


class LoginTest17(unittest.TestCase):
    driver = webdriver.Chrome()
    email_address = "sephoramajor@gmail.com"
    password = "antibacterie"
    @classmethod
    def setUpClass(cls):
        login = Login(cls.driver)
        cls.driver.get(login.url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_17(self):
        wait = WebDriverWait(self.driver, 10)
        login = Login(self.driver)
        # Click "Sign In" link
        login.close_icon()
        login.click_signin()
        # Enter valid email
        login.set_email_address(self.email_address)
        # Select "No, I am new to the website" radio button
        login.click_new_to_site()
        # Click "Continue" button
        login.click_continue()
        # Check if an error message appears, if no => error
        element = wait.until(EC.presence_of_element_located((By.XPATH, Login.alert_incorrect_pass)))
        assert element.is_displayed(), "ERROR. 'An account already exists' alert message doesn't appear."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="LoginTest17"))
