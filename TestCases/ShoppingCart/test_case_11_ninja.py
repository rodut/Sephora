import unittest
import HtmlTestRunner
from selenium import webdriver
from PageObjects.ShoppingCartNinja import ShoppingCartNinja
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"


class ShoppingCartTest11Ninja(unittest.TestCase):
    driver = webdriver.Chrome()
    email_address = "jacknicholson@gmail.com"
    password = "123456789"

    @classmethod
    def setUpClass(cls):
        cls.driver.maximize_window()
        shopcart = ShoppingCartNinja(cls.driver)
        cls.driver.get(shopcart.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_shopping_cart_11_ninja(self):
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
        # Click "Shopping Cart" link
        shopcart.click_shopping_cart()
        # Verify if a coupon code can be used only if a product is added to shopping cart
        element = self.driver.find_elements_by_xpath(ShoppingCartNinja.coupon_code)
        if len(element) > 0:
            sys.exit("ERROR. Coupon code can be used even if a product is not added to shopping cart.")
        else:
            print("OK. Coupon code can be used only if a product is added to shopping cart.")
        # Verity if a gift certificate can be used only if a product is added to shopping cart
        element = self.driver.find_elements_by_xpath(ShoppingCartNinja.gift_certificate)
        if len(element) > 0:
            sys.exit("ERROR. Gift certificate can be used even if a product is not added to shopping cart.")
        else:
            print("OK. Gift certificate can be used only if a product is added to shopping cart.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="ShoppingCartTest11Ninja"))
