import unittest
import HtmlTestRunner
from selenium import webdriver
from PageObjects.ShoppingCartNinja import ShoppingCartNinja
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"


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

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_shopping_cart_09_ninja(self):
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
        elem_1 = self.driver.find_elements_by_xpath(ShoppingCartNinja.price_item_1)
        for price in elem_1:
            x = price.text
            y = x.replace("Ex Tax: $", "")
            z = y.replace(".00", "")
            price_1 = int(z)
        new_price = price_1 * 5
        # Click on "Shopping Cart" link
        shopcart.click_shopping_cart()
        # Change the quantity from 1 to 5
        shopcart.set_quantity(self.quantity)
        # Click on "Update" button
        shopcart.click_update_button()
        # Verify is total sum is correct
        element = self.driver.find_elements_by_xpath(ShoppingCartNinja.total_price)
        for price in element:
            x = price.text
            y = x.replace("$", "")
            z = y.replace(".00", "")
            w = z.replace(",", "")
            total_price = int(w)
        assert new_price == total_price, "ERROR. The sum is incorrect."
        # Delete items in "Shopping Cart", it must be empty for the next test cases
        self.driver.refresh()
        shopcart.click_remove_button()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="ShoppingCartTest09Ninja"))
