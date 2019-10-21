import unittest
import HtmlTestRunner
import time
from selenium import webdriver
from PageObjects.ShoppingCartNinja import ShoppingCartNinja
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class ShoppingCartTest06Ninja(unittest.TestCase):
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

    def test_shopping_cart_06_ninja(self):
        shopcart = ShoppingCartNinja(self.driver)
        # Add to cart a random item
        element_1 = self.driver.find_element_by_xpath(ShoppingCartNinja.elem_1)
        elem_1 = element_1.text
        shopcart.click_add_item_1()
        # Click on "Shopping Cart" link
        shopcart.click_shopping_cart()
        # Verify if the product is present in the shopping cart
        element_2 = self.driver.find_element_by_xpath(ShoppingCartNinja.elem_2)
        elem_2 = element_2.text
        if elem_1 == elem_2:
            print("OK. User can view the selected book in the shopping cart.")
        else:
            sys.exit("ERROR. User cannot view the selected book in the shopping cart.")
        # Click "Checkout" button
        shopcart.click_checkout_button()
        time.sleep(1)
        # Verify if the site is asking you to login
        element = self.driver.find_element_by_xpath(ShoppingCartNinja.returning_customer).is_displayed()
        if element:
            print("OK. The site asks user to login.")
        else:
            sys.exit("ERROR. The site didn't asked user to login.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="ShoppingCartTest06Ninja"))
