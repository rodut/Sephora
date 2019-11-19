import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.Login import Login
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"


class LoginTest02(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        login = Login(cls.driver)
        cls.driver.get(login.url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_01(self):
        wait = WebDriverWait(self.driver, 10)
        login = Login(self.driver)
        # Clicking "Sign In" link
        login.close_icon()
        login.click_signin()
        # Verifying if 'Email address' field is present.
        element = wait.until(EC.presence_of_element_located((By.XPATH, Login.email_address_id)))
        assert element.is_displayed(), "ERROR. 'Email address' field is not present."
        # Verifying if 'No, I am new to the website' radio button is present.
        element = wait.until(EC.presence_of_element_located((By.XPATH, Login.no_password)))
        assert element.is_displayed(), "ERROR. 'No, I am new to the website' radio button is not present."
        # Verifying if 'Yes, I have a password' radio button is present.
        element = wait.until(EC.presence_of_element_located((By.XPATH, Login.yes_password)))
        assert element.is_displayed(), "ERROR. 'Yes, I have a password' radio button is not present."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="LoginTest01"))
