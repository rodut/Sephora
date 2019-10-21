import unittest
import HtmlTestRunner
import time
from selenium import webdriver
from PageObjects.ShoppingCartNinja import ShoppingCartNinja
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class ShoppingCartTest08Ninja(unittest.TestCase):
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

    def test_shopping_cart_08_ninja(self):
        shopcart = ShoppingCartNinja(self.driver)
        # Click on "My Account" link
        shopcart.click_my_account_link()
        # Click on "Login" link
        shopcart.click_login_link()
        # Enter an existing email address
        shopcart.set_email(self.email_address)
        # Enter an existing password
        shopcart.set_password(self.password)
        # Click "Login" button
        shopcart.click_login_button()
        # Go to main page
        shopcart.click_main_page()
        # Randomly select 2 products and add them to Shopping Cart
        shopcart.click_add_item_1()
        shopcart.click_add_item_2()
        # Save prices
        elem_1 = self.driver.find_elements_by_xpath(ShoppingCartNinja.price_item_1)
        for price in elem_1:
            x = price.text
            y = x.replace("Ex Tax: $", "")
            price_1 = float(y)
        elem_2 = self.driver.find_elements_by_xpath(ShoppingCartNinja.price_item_2)
        for price in elem_2:
            x = price.text
            y = x.replace("Ex Tax: $", "")
            price_2 = float(y)
        suma = price_1 + price_2
        # Click on "Shopping Cart" link
        shopcart.click_shopping_cart()
        # Verify is total sum is correct
        element = self.driver.find_elements_by_xpath(ShoppingCartNinja.total_price)
        for price in element:
            x = price.text
            y = x.replace("$", "")
            total_price = float(y)
        if suma == total_price:
            print("OK. The sum is correct.")
        else:
            sys.exit("ERROR. The sum is incorrect.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="ShoppingCartTest08Ninja"))
