import unittest
import HtmlTestRunner
import time
from selenium import webdriver
from PageObjects.ShoppingCartNinja import ShoppingCartNinja
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class ShoppingCartTest04Ninja(unittest.TestCase):
    driver = webdriver.Chrome()
    email_address = "jacknicholson@gmail.com"
    password = "123456789"

    @classmethod
    def setUpClass(cls):
        cls.driver.maximize_window()
        shopcart = ShoppingCartNinja(cls.driver)
        cls.driver.get(shopcart.url)
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_shopping_cart_04_ninja(self):
        shopcart = ShoppingCartNinja(self.driver)
        shopcart.click_my_account_link()
        shopcart.click_login_link()
        shopcart.set_email(self.email_address)
        shopcart.set_password(self.password)
        shopcart.click_login_button()
        shopcart.click_main_page()
        element_1 = self.driver.find_element_by_xpath(ShoppingCartNinja.elem_1)
        elem_1 = element_1.text
        shopcart.click_wish_list_button()
        shopcart.click_wish_list_link()
        element_2 = self.driver.find_element_by_xpath(ShoppingCartNinja.wishlist_elem)
        elem_2 = element_2.text
        if elem_1 == elem_2:
            print("OK. User can view the selected book in the Wish List.")
        else:
            sys.exit("ERROR. User cannot view the selected book in the Wish List.")
        shopcart.click_remove_button()
        element_2 = self.driver.find_elements_by_xpath(ShoppingCartNinja.wishlist_elem)
        if len(element_2) > 0:
            sys.exit("ERROR. The product wasn't remove from the wish list.")
        else:
            print("OK. The product was successfully removed from the wish list.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="ShoppingCartTest04Ninja"))
