import unittest
import HtmlTestRunner
import time
from selenium import webdriver
from PageObjects.MyAccountNinja import MyAccountNinja
import sys

sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class MyAccountTest03Ninja(unittest.TestCase):
    driver = webdriver.Chrome()
    email_address = "jacknicholson@gmail.com"
    password = "123456789"

    @classmethod
    def setUpClass(cls):
        cls.driver.maximize_window()
        shopcart = MyAccountNinja(cls.driver)
        cls.driver.get(shopcart.url)
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_my_account_03_ninja(self):
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

        # Check if the link under "My Affiliate Account" text is displayed
        element = self.driver.find_element_by_xpath(MyAccountNinja.reg_aff_acc_link).is_displayed()
        if element:
            print("OK. 'Register for an affiliate account' link is displayed.")
        else:
            sys.exit("ERROR. 'Register for an affiliate account' link is not displayed.")

        myacc.click_reg_aff_acc_link()
        element = self.driver.find_element_by_xpath(MyAccountNinja.verify_reg_aff_acc).is_displayed()
        if element:
            print("OK. 'Register for an affiliate account' link is working.")
        else:
            sys.exit("ERROR. 'Register for an affiliate account' link is broken.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="MyAccountTest03Ninja"))
