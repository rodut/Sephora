import unittest
import HtmlTestRunner
from selenium import webdriver
from PageObjects.ShoppingCartNinja import ShoppingCartNinja
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"


class ShoppingCartTest02Ninja(unittest.TestCase):
    driver = webdriver.Chrome()
    email_address = "jacknicholson@gmail.com"
    password = "123456789"

    @classmethod
    def setUpClass(cls):
        cls.driver.maximize_window()
        login = ShoppingCartNinja(cls.driver)
        cls.driver.get(login.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_shopping_cart_02_ninja(self):
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
        # Randomly select a product and click "Add to Wish List" button
        element_1 = self.driver.find_element_by_xpath(ShoppingCartNinja.elem_1)
        elem_1 = element_1.text
        login.click_wish_list_button()
        # Click on "Wish List" link
        login.click_wish_list_link()
        # Verify if the selected product is in "Wish List"
        element_2 = self.driver.find_element_by_xpath(ShoppingCartNinja.wishlist_elem)
        elem_2 = element_2.text
        assert elem_1 == elem_2, "ERROR. User cannot view the selected book in the Wish List."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="ShoppingCartTest02Ninja"))
