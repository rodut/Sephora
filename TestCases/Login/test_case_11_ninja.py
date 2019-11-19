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


class LoginTest11Ninja(unittest.TestCase):
    driver = webdriver.Chrome()
    email_address = "jacknicholson@gmail.com"
    password = "123456789"

    @classmethod
    def setUpClass(cls):
        login = LoginNinja(cls.driver)
        cls.driver.get(login.url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_11_ninja(self):
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
        # Click "Login" button
        login.click_login_button()
        # Click "Back Arrow" on browser button (2 times)
        login.windows_back_page()
        login.windows_back_page()
        # Click "My Account" link
        login.click_my_account_link()
        # Click "Login" link
        login.click_login_link()
        # Check if user is logged in, if not -> error (check if Logout link is present)
        element = wait.until(EC.presence_of_element_located((By.XPATH, LoginNinja.logout_link))).is_displayed()
        assert element, "ERROR. The user was logged out."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="LoginTest11Ninja"))
