import unittest
import HtmlTestRunner
from PageObjects.ShoppingCartNinja import ShoppingCartNinja
from selenium import webdriver
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"


class ShoppingCartTest10Ninja(unittest.TestCase):
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

    def test_shopping_cart_10_ninja(self):
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
        # Randomly select a product and add it to Shopping Cart
        shopcart.click_add_item_1()
        # Click on "My Account" link
        shopcart.click_my_account_link()
        # Click on "Logout" link
        shopcart.click_top_logout_link()
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
        # Verify if the selected product is still in the "Shopping Cart"
        element = self.driver.find_element_by_xpath(ShoppingCartNinja.verify_product).is_displayed()
        assert element, "ERROR. The product is not in shopping cart."
        # Delete items in "Shopping Cart", it must be empty for the next test cases
        self.driver.refresh()
        shopcart.click_remove_button()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="ShoppingCartTest10Ninja"))
