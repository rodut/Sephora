import unittest
import HtmlTestRunner
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from PageObjects.LoginNinja import LoginNinja
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"


class LoginTest14Ninja(unittest.TestCase):
    driver = webdriver.Chrome()
    email_address = "jacknicholson@gmail.com"
    password = "123456789"

    @classmethod
    def setUpClass(cls):
        cls.driver.maximize_window()
        login = LoginNinja(cls.driver)
        cls.driver.get(login.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_14_ninja(self):
        wait = WebDriverWait(self.driver, 10)
        login = LoginNinja(self.driver)
        # Click "My Account" link
        login.click_my_account_link()
        # Click "Login" link
        login.click_login_link()
        # Enter valid email
        login.set_email(self.email_address)
        # Enter valid password
        login.set_password(self.password)
        # Copy password (ctrl+c), than delete password, than paste password (ctrl+v)
        login.verify_password()
        # Click "Login" button
        login.click_login_button()
        # An warning should appear: "No match for E-Mail Address and/or Password."
        element = wait.until(EC.presence_of_element_located((By.XPATH, LoginNinja.warning_message))).is_displayed()
        assert element, "ERROR. User can copy/paste the password with asterisks."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="LoginTest14Ninja"))
