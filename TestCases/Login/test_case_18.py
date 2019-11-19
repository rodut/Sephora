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


class LoginTest18(unittest.TestCase):
    driver = webdriver.Chrome()
    email_address = "sephoramajordome11@gmail.com"
    password = "antibacterie"

    @classmethod
    def setUpClass(cls):
        login = Login(cls.driver)
        cls.driver.get(login.url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_18(self):
        wait = WebDriverWait(self.driver, 10)
        login = Login(self.driver)
        # Click "Sign In" link
        login.close_icon()
        login.click_signin()
        # Enter an unregistered email
        login.set_email_address(self.email_address)
        # Select "No, I am new to the website"
        login.click_new_to_site()
        # Click "Continue" button
        login.click_continue()
        # Check if a registration form appeared, if no => error
        element = wait.until(EC.presence_of_element_located((By.XPATH, Login.register_sephora)))
        assert element.is_displayed(), "ERROR. 'Register with Sephora' registration form doesn't appear."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="LoginTest18"))
