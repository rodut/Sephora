import unittest
import HtmlTestRunner
from PageObjects.Login import Login
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"


class LoginTest06(unittest.TestCase):
    driver = webdriver.Chrome()
    email_address = "abra@cadabra."
    password = "123456"

    @classmethod
    def setUpClass(cls):
        login = Login(cls.driver)
        cls.driver.get(login.url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_06(self):
        wait = WebDriverWait(self.driver, 10)
        login = Login(self.driver)
        # Clicking "Sign In" link
        login.close_icon()
        login.click_signin()
        # Enter a invalid email in email field
        login.set_email_address(self.email_address)
        # Enter a invalid password in password field
        login.set_password(self.password)
        # Click 'Continue' button
        login.click_continue()
        # Verify if alert email error text is present.
        element = wait.until(EC.presence_of_element_located((By.XPATH, Login.alert_incorrect_email)))
        assert element.is_displayed(), "ERROR. Alert email error text is no present."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="LoginTest06"))
