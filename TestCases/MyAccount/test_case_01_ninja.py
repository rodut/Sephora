import unittest
import HtmlTestRunner
import time
from selenium import webdriver
from PageObjects.MyAccountNinja import MyAccountNinja
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"


class MyAccountTest01Ninja(unittest.TestCase):
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

    def test_my_account_01_ninja(self):
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
        # Check if all links under "My Account" text are displayed
        element = self.driver.find_element_by_xpath(MyAccountNinja.edit_account_link).is_displayed()
        assert element, "ERROR. 'Edit Account' link is not displayed."
        # Check if password link is displayed
        element = self.driver.find_element_by_xpath(MyAccountNinja.password_link).is_displayed()
        assert element, "ERROR. 'Password' link is not displayed."
        # Check if address book link is displayed
        element = self.driver.find_element_by_xpath(MyAccountNinja.address_book_link).is_displayed()
        assert element, "ERROR. 'Address book' link is not displayed."
        # Check if wish list link is displayed
        element = self.driver.find_element_by_xpath(MyAccountNinja.wish_list_link).is_displayed()
        assert element, "ERROR. 'Wish List' link is not displayed."
        myacc.click_edit_account_link()
        element = self.driver.find_element_by_xpath(MyAccountNinja.verify_edit_account).is_displayed()
        assert element, "ERROR. 'Edit Account' link is broken."
        # Click back button
        myacc.click_back_button()
        # Click password link
        myacc.click_password_link()
        # Verify if password link is working
        element = self.driver.find_element_by_xpath(MyAccountNinja.verify_password_link).is_displayed()
        assert element, "ERROR. 'Password' link is broken."
        myacc.click_back_button()
        # Click address book link
        myacc.click_address_book_link()
        # Verify if address book link is displayed
        element = self.driver.find_element_by_xpath(MyAccountNinja.verify_address_book).is_displayed()
        assert element, "ERROR. 'Address book' link is broken."
        # Click back button
        myacc.click_back_button()
        # Click with list link
        myacc.click_wish_list_link()
        # Verify if wish list link is working
        element = self.driver.find_element_by_xpath(MyAccountNinja.verify_wish_list).is_displayed()
        assert element, "ERROR. ''Wish List' link is broken."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="MyAccountTest01Ninja"))
