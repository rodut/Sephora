import unittest
import HtmlTestRunner
import time
from selenium import webdriver
from PageObjects.ShoppingCartNinja import ShoppingCartNinja
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class ShoppingCartTest05Ninja(unittest.TestCase):
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

    def test_shopping_cart_05_ninja(self):
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
        # Randomly select a product and click "Add to Wish List" button
        element_1 = self.driver.find_element_by_xpath(ShoppingCartNinja.elem_1)
        elem_1 = element_1.text
        shopcart.click_wish_list_button()
        # Click on "Wish List" link
        shopcart.click_wish_list_link()
        # Verify if the selected product is in "Wish List"
        element_2 = self.driver.find_element_by_xpath(ShoppingCartNinja.wishlist_elem)
        elem_2 = element_2.text
        if elem_1 == elem_2:
            print("OK. User can view the selected book in the Wish List.")
        else:
            sys.exit("ERROR. User cannot view the selected book in the Wish List.")
        # Click on "Add to Cart" button
        shopcart.click_addtocart_button()
        # Click On "Shopping Cart" link
        shopcart.click_shopping_cart()
        # Verify if the product was moved to "Shopping Cart"
        element_2 = self.driver.find_element_by_xpath(ShoppingCartNinja.elem_2).is_displayed()
        if element_2:
            print("OK. The product was moved to Shopping Cart.")
        else:
            sys.exit("ERROR. The product wasn't moved to Shopping Cart.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="ShoppingCartTest05Ninja"))
