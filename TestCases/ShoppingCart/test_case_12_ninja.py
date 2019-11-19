import unittest
import HtmlTestRunner
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from PageObjects.ShoppingCartNinja import ShoppingCartNinja
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class ShoppingCartTest12Ninja(unittest.TestCase):
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
        time.sleep(600)
        cls.driver.quit()

    def test_shopping_cart_12_ninja(self):
        wait = WebDriverWait(self.driver, 10)
        shopcart = ShoppingCartNinja(self.driver)
        # Add to cart a random item
        element_1 = self.driver.find_element_by_xpath(ShoppingCartNinja.elem_1)
        elem_1 = element_1.text
        shopcart.click_add_item_1()
        # Click on "Shopping Cart" link
        shopcart.click_shopping_cart()
        # Verify if the product is present
        element_2 = self.driver.find_element_by_xpath(ShoppingCartNinja.elem_2)
        elem_2 = element_2.text
        assert elem_1 == elem_2, "ERROR. User cannot view the selected book in the shopping cart."
        # Click "Checkout" button
        shopcart.click_checkout_button()
        # Verify if the site is asking you to login
        element = wait.until(EC.presence_of_element_located((By.XPATH, ShoppingCartNinja.returning_customer))).is_displayed()
        assert element, "ERROR. The site didn't asked user to login."
        # Enter a valid email address
        shopcart.set_email(self.email_address)
        # Enter a valid password
        shopcart.set_password(self.password)
        # Click "Login" button
        shopcart.click_checkout_login_button()
        # Click "Shopping Cart" link
        shopcart.click_shopping_cart()
        # Verify if the product was added to the shopping cart
        element_2 = wait.until(EC.presence_of_element_located((By.XPATH, ShoppingCartNinja.elem_2)))
        elem_2 = element_2.text
        assert elem_1 == elem_2, "ERROR. Logged in user cannot view the selected book in the shopping cart."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="ShoppingCartTest12Ninja"))
