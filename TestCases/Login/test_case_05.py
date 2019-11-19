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
__email__  = "tudorache@gmail.com"


class LoginTest05(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        login = Login(cls.driver)
        cls.driver.get(login.url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_05(self):
        wait = WebDriverWait(self.driver, 10)
        login = Login(self.driver)
        # Clicking "Sign In" link
        login.close_icon()
        login.click_signin()
        # Verifying if 'What is your email address' text is present.
        element = wait.until(EC.presence_of_element_located((By.XPATH, Login.what_email_address)))
        assert element.is_displayed(), "ERROR. 'What is your email address' text is not present."
        # Verifying if 'Do you have a sephora.com password?' text is present.
        element = wait.until(EC.presence_of_element_located((By.XPATH, Login.have_sephora_password)))
        assert element.is_displayed(), "ERROR. 'Do you have a sephora.com password?' text is not present."
        # Verifying if 'Have a Beauty Insider account?' text is present.
        element = wait.until(EC.presence_of_element_located((By.XPATH, Login.have_beauty_text)))
        assert element.is_displayed(), "ERROR. 'Have a Beauty Insider account?' text is not present."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="LoginTest05"))
