import unittest
import HtmlTestRunner
import time
from selenium import webdriver
from PageObjects.MyAccountNinja import MyAccountNinja
import sys

sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


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
        myacc.click_my_account_link()
        myacc.click_login_link()
        myacc.set_email(self.email_address)
        myacc.set_password(self.password)
        myacc.click_login_button()
        myacc.click_edit_account_link()
        myacc.set_first_name(self.first_name)
        myacc.set_last_name(self.last_name)
        myacc.set_new_email(self.new_email)
        myacc.set_telephone(self.telephone)
        myacc.click_continue_button()
        myacc.click_edit_account_link()
        new_first_name = "Jacky"
        new_last_name = "Boy"
        new_email_address = "abracadabra@gmail.com"
        new_telephone = "+121233344455"
        elem = self.driver.find_element_by_xpath(MyAccountNinja.first_name_field)
        element = elem.get_attribute("value")
        time.sleep(2)
        if element == new_first_name:
            print("OK. First name has been changed successfully.")
        else:
            sys.exit("ERROR. First name hasn't been changed.")
        elem = self.driver.find_element_by_xpath(MyAccountNinja.last_name_field)
        element = elem.get_attribute("value")
        if element == new_last_name:
            print("OK. Last name has been changed successfully.")
        else:
            sys.exit("ERROR. Last name hasn't been changed.")
        elem = self.driver.find_element_by_xpath(MyAccountNinja.email_field)
        element = elem.get_attribute("value")
        if element == new_email_address:
            print("OK. E-Mail has been changed successfully.")
        else:
            sys.exit("ERROR. E-Mail hasn't been changed.")
        elem = self.driver.find_element_by_xpath(MyAccountNinja.telephone_field)
        element = elem.get_attribute("value")
        if element == new_telephone:
            print("OK. Telephone has been changed successfully.")
        else:
            sys.exit("ERROR. Telephone hasn't been changed.")
        myacc.set_new_email(self.email_address)
        myacc.click_continue_button()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="MyAccountTest06Ninja"))
