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


class LoginTest10(unittest.TestCase):
    driver = webdriver.Chrome()
    email_address = ""
    password = ""
    @classmethod
    def setUpClass(cls):
        login = Login(cls.driver)
        cls.driver.get(login.url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_10(self):
        wait = WebDriverWait(self.driver, 10)
        login = Login(self.driver)
        # Clicking "Sign In" link
        login.close_icon()
        login.click_signin()
        # Enter an empty email in email field
        login.set_email_address(self.email_address)
        # Enter an empty password in password field
        login.set_password(self.password)
        # Click on "Continue" button
        login.click_continue()
        # Verify if user cannot login with empty email and empty pass
        element = wait.until(EC.presence_of_element_located((By.XPATH, Login.alert_no_email_address)))
        assert element.is_displayed(), "ERROR. Missing email error text is no present."
        element = wait.until(EC.presence_of_element_located((By.XPATH, Login.alert_pass_missing)))
        assert element.is_displayed(), "ERROR. password email error text is no present."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="LoginTest10"))
