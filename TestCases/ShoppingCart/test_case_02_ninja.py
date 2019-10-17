import unittest
import HtmlTestRunner
import time
from selenium import webdriver
from PageObjects.ShoppingCartNinja import ShoppingCartNinja
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class ShoppingCartTest02Ninja(unittest.TestCase):
    driver = webdriver.Chrome()
    email_address = "jacknicholson@gmail.com"
    password = "123456789"

    @classmethod
    def setUpClass(cls):
        cls.driver.maximize_window()
        login = ShoppingCartNinja(cls.driver)
        cls.driver.get(login.url)
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_shopping_cart_02_ninja(self):
        login = ShoppingCartNinja(self.driver)
        login.click_my_account_link()
        login.click_login_link()
        login.set_email(self.email_address)
        login.set_password(self.password)
        login.click_login_button()
        login.click_main_page()
        element_1 = self.driver.find_element_by_xpath(ShoppingCartNinja.elem_1)
        elem_1 = element_1.text
        login.click_wish_list_button()
        login.click_wish_list_link()
        element_2 = self.driver.find_element_by_xpath(ShoppingCartNinja.wishlist_elem)
        elem_2 = element_2.text
        if elem_1 == elem_2:
            print("OK. User can view the selected book in the Wish List.")
        else:
            sys.exit("ERROR. User cannot view the selected book in the Wish List.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="ShoppingCartTest02Ninja"))
