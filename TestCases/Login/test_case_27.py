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


class LoginTest27(unittest.TestCase):
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

    def test_login_27(self):
        wait = WebDriverWait(self.driver, 10)
        login = Login(self.driver)
        # Click "Sign In" link
        login.close_icon()
        login.click_signin()
        # Select "No, I am new to the website" radio button
        login.click_new_to_site()
        # Check if password field disappeared, if it's present => error
        element = self.driver.find_elements_by_xpath(Login.password_field)
        assert len(element) == 0, "ERROR. The password field didn't disappear."
        # Select "Yes, I have a password"
        login.click_new_to_site()
        # Check if password field reappeared, if not =? error
        element = wait.until(EC.presence_of_element_located((By.XPATH, Login.password_field)))
        assert element.is_displayed(), "ERROR. The password field didn't reappear."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="LoginTest27"))
