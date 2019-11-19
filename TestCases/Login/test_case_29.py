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


class LoginTest29(unittest.TestCase):
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

    def test_login_29(self):
        wait = WebDriverWait(self.driver, 10)
        login = Login(self.driver)
        # Click "Sign In" link
        login.close_icon()
        login.click_signin()
        # 3. Click "Terms of Use" link
        login.click_terms_of_use()
        # Check if "Terms of Use" page has opened, if no => error
        element = wait.until(EC.presence_of_element_located((By.XPATH, Login.check_terms_of_use)))
        assert element.is_displayed(), "ERROR.  The user cannot see Terms of Use."
        # Click "X" in the right top corner
        login.click_close_terns_of_use()
        # Check if user returned to "Sign In" page
        element = wait.until(EC.presence_of_element_located((By.XPATH, Login.check_please_signin)))
        assert element.is_displayed(), "ERROR. User didn't return to Sign In page."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="LoginTest29"))
