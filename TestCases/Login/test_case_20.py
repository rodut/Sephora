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
__email__  = "tudorache@gmail.com"


class LoginTest20(unittest.TestCase):
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

    def test_login_20(self):
        wait = WebDriverWait(self.driver, 10)
        login = Login(self.driver)
        # Click "Sign In" link
        login.close_icon()
        login.click_signin()
        # Enter valid email
        login.set_email_address(self.email_address)
        # Click "Forgot?" link
        login.click_forgot_link()
        # Check if the entered email is present in email field
        element = wait.until(EC.presence_of_element_located((By.XPATH, Login.check_forgot_email)))
        assert element.is_displayed(), "ERROR. Previously entered email is not present in email field."
        # Click "Send Email" button
        login.click_send_email_button()
        # Check if a message with "reset password" is present
        element = wait.until(EC.presence_of_element_located((By.XPATH, Login.reset_password)))
        assert element.is_displayed(), "ERROR. There is no message with 'Reset Password' present"


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="LoginTest20"))
