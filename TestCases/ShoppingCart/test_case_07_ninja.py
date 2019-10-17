import unittest
import HtmlTestRunner
import time
from selenium import webdriver
from PageObjects.ShoppingCartNinja import ShoppingCartNinja
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class ShoppingCartTest07Ninja(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        cls.driver.maximize_window()
        shopcart = ShoppingCartNinja(cls.driver)
        cls.driver.get(shopcart.url)
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_shopping_cart_07_ninja(self):
        shopcart = ShoppingCartNinja(self.driver)
        shopcart.click_add_item_1()
        time.sleep(1)
        shopcart.click_black_button_id()
        shopcart.click_black_button_remove()
        time.sleep(1)
        shopcart.click_black_button_id()
        element = self.driver.find_element_by_xpath(ShoppingCartNinja.black_button_empty_text).is_displayed()
        if element:
            print("OK. User removed the item from shopping cart successfully.")
        else:
            sys.exit("ERROR. The item hasn't been removed from shopping cart.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="ShoppingCartTest07Ninja"))
