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


class LoginTest03(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        login = Login(cls.driver)
        cls.driver.get(login.url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_03(self):
        wait = WebDriverWait(self.driver, 10)
        login = Login(self.driver)
        # Clicking "Sign In" link
        login.close_icon()
        login.click_signin()
        # Verifying if 'Password' field is present.
        element = wait.until(EC.presence_of_element_located((By.XPATH, Login.password_field)))
        assert element.is_displayed(), "ERROR. 'Password' field is not present."
        # Verifying if 'Forgot?' link is present.
        element = wait.until(EC.presence_of_element_located((By.XPATH, Login.forgot_link)))
        assert element.is_displayed(), "ERROR. 'Forgot?' link is not present."
        # Verifying if 'Cancel' button is present.
        element = wait.until(EC.presence_of_element_located((By.XPATH, Login.cancel_button)))
        assert element.is_displayed(), "ERROR. 'Cancel' button is not present."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="LoginTest03"))
