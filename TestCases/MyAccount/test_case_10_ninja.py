import unittest
import HtmlTestRunner
import time
from selenium import webdriver
from PageObjects.MyAccountNinja import MyAccountNinja
import sys

sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class MyAccountTest10Ninja(unittest.TestCase):
    driver = webdriver.Chrome()
    email_address = "jacknicholson@gmail.com"
    password = "123456789"
    new_first_name = "Bobbi"
    new_last_name = "Starr"
    new_city = "Dallas"
    new_zip = "55555"
    new_address = "123 Main St."

    @classmethod
    def setUpClass(cls):
        cls.driver.maximize_window()
        shopcart = MyAccountNinja(cls.driver)
        cls.driver.get(shopcart.url)
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_my_account_10_ninja(self):
        myacc = MyAccountNinja(self.driver)
        myacc.click_my_account_link()
        myacc.click_login_link()
        myacc.set_email(self.email_address)
        myacc.set_password(self.password)
        myacc.click_login_button()
        myacc.click_address_book_link()
        myacc.click_new_address_button()
        myacc.set_new_address_first_name(self.new_first_name)
        myacc.set_new_address_last_name(self.new_last_name)
        myacc.set_new_address(self.new_address)
        myacc.set_new_address_city(self.new_city)
        myacc.set_new_address_zip(self.new_zip)
        time.sleep(1)
        myacc.set_country_usa()
        time.sleep(1)
        myacc.set_state_texas()
        myacc.select_yes_radio_button()
        myacc.click_continue_button()
        time.sleep(1)
        myacc.click_new_address_edit_button()
        myacc.select_no_radio_button()
        myacc.click_continue_button()
        myacc.click_new_address_edit_button()
        element = self.driver.find_element_by_xpath(MyAccountNinja.yes_radio_button).is_selected()
        if element:
            print("OK. 'Yes' radio button is still selected.")
        else:
            sys.exit("ERROR.'Yes' radio button is not selected.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="MyAccountTest10Ninja"))
