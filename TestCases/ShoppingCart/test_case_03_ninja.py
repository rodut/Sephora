import unittest
import HtmlTestRunner
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from PageObjects.ShoppingCartNinja import ShoppingCartNinja
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")
import time

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class ShoppingCartTest03Ninja(unittest.TestCase):
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

    def test_shopping_cart_03_ninja(self):
        wait = WebDriverWait(self.driver, 10)
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
        # Randomly select a product and click "Add to cart" button
        element_1 = self.driver.find_element_by_xpath(ShoppingCartNinja.elem_1)
        elem_1 = element_1.text
        shopcart.click_add_item_1()
        # Click on "Shopping Cart" link
        shopcart.click_shopping_cart()
        # Verify if selected product is in "Shopping Cart"
        element_2 = self.driver.find_element_by_xpath(ShoppingCartNinja.elem_2)
        elem_2 = element_2.text
        assert elem_1 == elem_2, "ERROR. User cannot view the selected book in the shopping cart."
        # Click on "Remove" button
        shopcart.click_remove_button()
        # Verify if the product was deleted
#        element_2 = wait.until(EC.presence_of_element_located((By.XPATH, ShoppingCartNinja.elem_2)))
        element_2 = wait.until(EC.invisibility_of_element_located((By.XPATH, ShoppingCartNinja.elem_2)))
        assert element_2, "ERROR. The product wasn't remove from the shopping cart."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="ShoppingCartTest03Ninja"))
