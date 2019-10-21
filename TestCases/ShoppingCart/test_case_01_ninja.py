import unittest
import HtmlTestRunner
import time
from selenium import webdriver
from PageObjects.ShoppingCartNinja import ShoppingCartNinja
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class ShoppingCartTest01Ninja(unittest.TestCase):
    driver = webdriver.Chrome()
    email_address = "jacknicholson@gmail.com"
    password = "123456789"

    @classmethod
    def setUpClass(cls):
        cls.driver.maximize_window()
        login = ShoppingCartNinja(cls.driver)
        cls.driver.get(login.url)
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_shopping_cart_01_ninja(self):
        login = ShoppingCartNinja(self.driver)
        # Click on "My Account" link
        login.click_my_account_link()
        # Click on "Login" link
        login.click_login_link()
        # Enter an existing email address
        login.set_email(self.email_address)
        # Enter an existing password
        login.set_password(self.password)
        # Click "Login" button
        login.click_login_button()
        # Go to main page
        login.click_main_page()
        # Randomly select a product and click "Add to cart" button
        element_1 = self.driver.find_element_by_xpath(ShoppingCartNinja.elem_1)
        elem_1 = element_1.text
        login.click_add_item_1()
        # Click on "Shopping Cart" link
        login.click_shopping_cart()
        # Verify if the selected product is present in shopping cart
        element_2 = self.driver.find_element_by_xpath(ShoppingCartNinja.elem_2)
        elem_2 = element_2.text
        if elem_1 == elem_2:
            print("OK. User can view the selected book in the shopping cart.")
        else:
            sys.exit("ERROR. User cannot view the selected book in the shopping cart.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="ShoppingCartTest01Ninja"))
