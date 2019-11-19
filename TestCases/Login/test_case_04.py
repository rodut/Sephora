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


class LoginTest04(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        login = Login(cls.driver)
        cls.driver.get(login.url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_04(self):
        wait = WebDriverWait(self.driver, 10)
        login = Login(self.driver)
        # Clicking "Sign In" link
        login.close_icon()
        login.click_signin()
        # Verifying if 'Continue' button is present.
        element = wait.until(EC.presence_of_element_located((By.XPATH, Login.continue_button)))
        assert element.is_displayed(), "ERROR. 'Continue' button is not present."
        # Verifying if 'Terms of Use' link is present.
        element = wait.until(EC.presence_of_element_located((By.XPATH, Login.terms_of_use_link)))
        assert element.is_displayed(), "ERROR. 'Terms of Use' link is not present."
        # Verifying if 'Privacy Policy' link is present.
        element = wait.until(EC.presence_of_element_located((By.XPATH, Login.privacy_policy_link)))
        assert element.is_displayed(), "ERROR. 'Privacy Policy' link is present."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="LoginTest04"))
