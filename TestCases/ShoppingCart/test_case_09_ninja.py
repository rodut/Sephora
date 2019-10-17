import unittest
import HtmlTestRunner
import time
from selenium import webdriver
from PageObjects.ShoppingCartNinja import ShoppingCartNinja
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class ShoppingCartTest09Ninja(unittest.TestCase):
    driver = webdriver.Chrome()
    email_address = "jacknicholson@gmail.com"
    password = "123456789"
    quantity = "5"

    @classmethod
    def setUpClass(cls):
        cls.driver.maximize_window()
        shopcart = ShoppingCartNinja(cls.driver)
        cls.driver.get(shopcart.url)
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_shopping_cart_09_ninja(self):
        shopcart = ShoppingCartNinja(self.driver)
        shopcart.click_my_account_link()
        shopcart.click_login_link()
        shopcart.set_email(self.email_address)
        shopcart.set_password(self.password)
        shopcart.click_login_button()
        shopcart.click_main_page()
        shopcart.click_add_item_1()
        elem_1 = self.driver.find_elements_by_xpath(ShoppingCartNinja.price_item_1)
        for price in elem_1:
            x = price.text
            y = x.replace("Ex Tax: $", "")
            z = y.replace(".00", "")
            price_1 = int(z)
        new_price = price_1 * 5
        shopcart.click_shopping_cart()
        shopcart.set_quantity(self.quantity)
        shopcart.click_update_button()
        element = self.driver.find_elements_by_xpath(ShoppingCartNinja.total_price)
        for price in element:
            x = price.text
            y = x.replace("$", "")
            z = y.replace(".00", "")
            w = z.replace(",", "")
            total_price = int(w)
        if new_price == total_price:
            print("OK. The sum is correct.")
        else:
            sys.exit("ERROR. The sum is incorrect.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="ShoppingCartTest09Ninja"))
