import unittest
import HtmlTestRunner
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.MyAccountNinja import MyAccountNinja
import sys

sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class MyAccountTest12Ninja(unittest.TestCase):
    driver = webdriver.Chrome()
    email_address = "jacknicholson@gmail.com"
    password = "123456789"
    first_name = "abracadabraabracadabraabracadabra"
    last_name = "abracadabraabracadabraabracadabra"
    email_empty ="jacknicholson@gmailcom"
    telephone = "abracadabraabracadabraabracadabra"

    @classmethod
    def setUpClass(cls):
        cls.driver.maximize_window()
        shopcart = MyAccountNinja(cls.driver)
        cls.driver.get(shopcart.url)
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_my_account_12_ninja(self):
        wait = WebDriverWait(self.driver, 10)
        myacc = MyAccountNinja(self.driver)
        # Click on "My Account" link
        myacc.click_my_account_link()
        # Click on "Login" link
        myacc.click_login_link()
        # Enter a valid email address
        myacc.set_email(self.email_address)
        # Enter a valid password
        myacc.set_password(self.password)
        # Click on "Login" button
        myacc.click_login_button()
        # Click on "Edit Account" link
        myacc.click_edit_account_link()
        # Enter more than 32 characters in "First Name" field
        myacc.set_first_name(self.first_name)
        # Enter more than 32 characters in "Last Name" field
        myacc.set_last_name(self.last_name)
        # Enter an invalid email in "E-Mail" field
        myacc.set_email(self.email_empty)
        # Enter more than 32 characters in "Telephone" field
        myacc.set_telephone(self.telephone)
        # Click "Continue" button
        myacc.click_continue_button()
        # Verify if error messages are present for every field
        element = wait.until(EC.presence_of_element_located((By.XPATH, MyAccountNinja.warning_first_name))).is_displayed()
        assert element, "ERROR. 'First Name' warning text is not displayed."
        element = self.driver.find_element_by_xpath(MyAccountNinja.warning_last_name).is_displayed()
        assert element, "ERROR. 'Last Name' warning text is not displayed."
        element = self.driver.find_element_by_xpath(MyAccountNinja.warning_email).is_displayed()
        assert element, "ERROR. 'E-mail' warning text is not displayed."
        element = self.driver.find_element_by_xpath(MyAccountNinja.warning_telephone).is_displayed()
        assert element, "ERROR. 'Telephone' warning text is not displayed."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="MyAccountTest12Ninja"))
