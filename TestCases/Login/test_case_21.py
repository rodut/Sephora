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


class LoginTest21(unittest.TestCase):
    driver = webdriver.Chrome()
    email_address = "sephoramajordome3500@gmail.com"
    password = "antibacterie"
    @classmethod
    def setUpClass(cls):
        login = Login(cls.driver)
        cls.driver.get(login.url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_21(self):
        wait = WebDriverWait(self.driver, 10)
        login = Login(self.driver)
        # Click "Sign In" link
        login.close_icon()
        login.click_signin()
        # Enter an invalid email
        login.set_email_address(self.email_address)
        # Click "Forgot?" link
        login.click_forgot_link()
        # Check if previously entered email is present in email field
        element = wait.until(EC.presence_of_element_located((By.XPATH, Login.check_invalid_forgot_email)))
        assert element.is_displayed(), "ERROR. Previously entered email is not present in email field."
        # Click "Send Email" button
        login.click_send_email_button()
        # Check if there is an error message regarding the email
        element = wait.until(EC.presence_of_element_located((By.XPATH, Login.alert_send_email)))
        assert element.is_displayed(), "ERROR. No alert text message is present."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="LoginTest21"))
