import unittest
import HtmlTestRunner
from selenium import webdriver
from PageObjects.ShoppingCartNinja import ShoppingCartNinja
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"


class ShoppingCartTest07Ninja(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        cls.driver.maximize_window()
        shopcart = ShoppingCartNinja(cls.driver)
        cls.driver.get(shopcart.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_shopping_cart_07_ninja(self):
        shopcart = ShoppingCartNinja(self.driver)
        # Add to cart a random item
        shopcart.click_add_item_1()
        # Click on black button (right up corner)
        shopcart.click_black_button_id()
        # Click on "Remove" button
        shopcart.click_black_button_remove()
        shopcart.click_black_button_id()
        # Verify if the item was removed
        element = self.driver.find_element_by_xpath(ShoppingCartNinja.black_button_empty_text).is_displayed()
        assert element, "ERROR. The item hasn't been removed from shopping cart."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="ShoppingCartTest07Ninja"))
