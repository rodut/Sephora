import unittest
import HtmlTestRunner
import time
from selenium import webdriver
from PageObjects.MyAccountNinja import MyAccountNinja
import sys

sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class MyAccountTest05Ninja(unittest.TestCase):
    driver = webdriver.Chrome()
    email_address = "jacknicholson@gmail.com"
    password = "123456789"
    first_name = ""
    last_name = ""
    email_empty = ""
    telephone = ""

    @classmethod
    def setUpClass(cls):
        cls.driver.maximize_window()
        shopcart = MyAccountNinja(cls.driver)
        cls.driver.get(shopcart.url)
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_my_account_05_ninja(self):
        myacc = MyAccountNinja(self.driver)
        myacc.click_my_account_link()
        myacc.click_login_link()
        myacc.set_email(self.email_address)
        myacc.set_password(self.password)
        myacc.click_login_button()
        myacc.click_edit_account_link()
        myacc.set_first_name(self.first_name)
        myacc.set_last_name(self.last_name)
        myacc.set_email(self.email_empty)
        myacc.set_telephone(self.telephone)
        myacc.click_continue_button()
        element = self.driver.find_element_by_xpath(MyAccountNinja.warning_first_name).is_displayed()
        if element:
            print("OK. 'First Name' warning text is displayed.")
        else:
            sys.exit("ERROR. 'First Name' warning text is not displayed.")
        element = self.driver.find_element_by_xpath(MyAccountNinja.warning_last_name).is_displayed()
        if element:
            print("OK. 'Last Name' warning text is displayed.")
        else:
            sys.exit("ERROR. 'Last Name' warning text is not displayed.")
        element = self.driver.find_element_by_xpath(MyAccountNinja.warning_email).is_displayed()
        if element:
            print("OK. 'E-mail' warning text is displayed.")
        else:
            sys.exit("ERROR. 'E-mail' warning text is not displayed.")
        element = self.driver.find_element_by_xpath(MyAccountNinja.warning_telephone).is_displayed()
        if element:
            print("OK. 'Telephone' warning text is displayed.")
        else:
            sys.exit("ERROR. 'Telephone' warning text is not displayed.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="MyAccountTest05Ninja"))
