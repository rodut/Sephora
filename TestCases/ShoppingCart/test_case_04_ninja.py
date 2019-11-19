import unittest
import HtmlTestRunner
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from PageObjects.ShoppingCartNinja import ShoppingCartNinja
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"


class ShoppingCartTest04Ninja(unittest.TestCase):
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

    def test_shopping_cart_04_ninja(self):
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
        # Randomly select a product and click "Add to Wish List" button
        element_1 = self.driver.find_element_by_xpath(ShoppingCartNinja.elem_1)
        elem_1 = element_1.text
        shopcart.click_wish_list_button()
        # Click on "Wish List" link
        shopcart.click_wish_list_link()
        # Verify if the selected product is in "Wish List"
        element_2 = self.driver.find_element_by_xpath(ShoppingCartNinja.wishlist_elem)
        elem_2 = element_2.text
        assert elem_1 == elem_2, "ERROR. User cannot view the selected book in the Wish List."
        # Click on "Remove" button
        shopcart.click_remove_button()
        # Verify if product was deleted
        element_2 = wait.until(EC.invisibility_of_element_located((By.XPATH, ShoppingCartNinja.wishlist_elem)))
        assert element_2, "OK. The product was successfully removed from the wish list."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="ShoppingCartTest04Ninja"))
