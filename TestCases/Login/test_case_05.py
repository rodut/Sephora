import unittest
import HtmlTestRunner
from PageObjects.Login import Login
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
        login = Login(self.driver)
        # Clicking "Sign In" link
        login.close_icon()
        login.click_signin()
        # Verifying if 'What is your email address' text is present.
        element = self.driver.find_elements_by_xpath(Login.what_email_address)
        if len(element) > 0:
            print("OK. 'What is your email address' text is present.")
        else:
            sys.exit("ERROR. 'What is your email address' text is not present.")
        # Verifying if 'Do you have a sephora.com password?' text is present.
        element = self.driver.find_elements_by_xpath(Login.have_sephora_password)
        if len(element) > 0:
            print("OK. 'Do you have a sephora.com password?' text is present.")
        else:
            sys.exit("ERROR. 'Do you have a sephora.com password?' text is not present.")
        # Verifying if 'Have a Beauty Insider account?' text is present.
        element = self.driver.find_elements_by_xpath(Login.have_beauty_text)
        if len(element) > 0:
            print("OK. 'Have a Beauty Insider account?' text is present.")
        else:
            sys.exit("ERROR. 'Have a Beauty Insider account?' text is not present.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="LoginTest05"))
