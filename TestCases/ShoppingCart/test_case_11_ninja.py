import unittest
import HtmlTestRunner
import time
from selenium import webdriver
from PageObjects.ShoppingCartNinja import ShoppingCartNinja
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class ShoppingCartTest11Ninja(unittest.TestCase):
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

    def test_shopping_cart_11_ninja(self):
        shopcart = ShoppingCartNinja(self.driver)
        shopcart.click_my_account_link()
        shopcart.click_login_link()
        shopcart.set_email(self.email_address)
        shopcart.set_password(self.password)
        shopcart.click_login_button()
        shopcart.click_shopping_cart()
        element = self.driver.find_elements_by_xpath(ShoppingCartNinja.coupon_code)
        if len(element) > 0:
            sys.exit("ERROR. Coupon code can be used even if a product is not added to shopping cart.")
        else:
            print("OK. Coupon code can be used only if a product is added to shopping cart.")
        element = self.driver.find_elements_by_xpath(ShoppingCartNinja.gift_certificate)
        if len(element) > 0:
            sys.exit("ERROR. Gift certificate can be used even if a product is not added to shopping cart.")
        else:
            print("OK. Gift certificate can be used only if a product is added to shopping cart.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="ShoppingCartTest11Ninja"))
