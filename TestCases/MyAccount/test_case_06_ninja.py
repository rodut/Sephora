import unittest
import HtmlTestRunner
import time
from selenium import webdriver
from PageObjects.MyAccountNinja import MyAccountNinja
import sys

sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"


class MyAccountTest06Ninja(unittest.TestCase):
    driver = webdriver.Chrome()
    email_address = "jacknicholson@gmail.com"
    password = "123456789"
    first_name = "Jacky"
    last_name = "Boy"
    new_email = "abracadabra@gmail.com"
    telephone = "+121233344455"

    @classmethod
    def setUpClass(cls):
        cls.driver.maximize_window()
        shopcart = MyAccountNinja(cls.driver)
        cls.driver.get(shopcart.url)
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_my_account_06_ninja(self):
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
        # Enter new "First Name"
        myacc.set_first_name(self.first_name)
        # Enter new "Last Name"
        myacc.set_last_name(self.last_name)
        # Enter new "E-Mail"
        myacc.set_new_email(self.new_email)
        # Enter new "Telephone"
        myacc.set_telephone(self.telephone)
        # Click on "Continue" button
        myacc.click_continue_button()
        # Click "Edit Account"
        myacc.click_edit_account_link()
        # Verify if all the field changed with new data
        new_first_name = "Jacky"
        new_last_name = "Boy"
        new_email_address = "abracadabra@gmail.com"
        new_telephone = "+121233344455"
        elem = self.driver.find_element_by_xpath(MyAccountNinja.first_name_field)
        element = elem.get_attribute("value")
        time.sleep(2)
        #
        assert element == new_first_name, "ERROR. First name hasn't been changed."
        elem = self.driver.find_element_by_xpath(MyAccountNinja.last_name_field)
        element = elem.get_attribute("value")
        assert element == new_last_name, "ERROR. Last name hasn't been changed."
        elem = self.driver.find_element_by_xpath(MyAccountNinja.email_field)
        element = elem.get_attribute("value")
        assert element == new_email_address, "ERROR. E-Mail hasn't been changed."
        elem = self.driver.find_element_by_xpath(MyAccountNinja.telephone_field)
        element = elem.get_attribute("value")
        assert element == new_telephone, "ERROR. Telephone hasn't been changed."
        myacc.set_new_email(self.email_address)
        myacc.click_continue_button()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="MyAccountTest06Ninja"))
