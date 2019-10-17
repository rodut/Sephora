import unittest
import HtmlTestRunner
import time
from PageObjects.ShoppingCartNinja import ShoppingCartNinja
from selenium import webdriver
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class ShoppingCartTest10Ninja(unittest.TestCase):
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

    def test_shopping_cart_10_ninja(self):
        shopcart = ShoppingCartNinja(self.driver)
        shopcart.click_my_account_link()
        shopcart.click_login_link()
        shopcart.set_email(self.email_address)
        shopcart.set_password(self.password)
        shopcart.click_login_button()
        shopcart.click_main_page()
        shopcart.click_add_item_1()
        shopcart.click_my_account_link()
        shopcart.click_top_logout_link()
        shopcart.click_my_account_link()
        shopcart.click_login_link()
        shopcart.set_email(self.email_address)
        shopcart.set_password(self.password)
        shopcart.click_login_button()
        shopcart.click_shopping_cart()
        element = self.driver.find_element_by_xpath(ShoppingCartNinja.verify_product).is_displayed()
        if element:
            print("OK. The product is still in shopping cart.")
        else:
            sys.exit("ERROR. The product is not in shopping cart.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="ShoppingCartTest10Ninja"))
