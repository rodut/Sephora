import unittest
import HtmlTestRunner
import time
from selenium import webdriver
from PageObjects.MyAccountNinja import MyAccountNinja
import sys

sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class MyAccountTest02Ninja(unittest.TestCase):
    driver = webdriver.Chrome()
    email_address = "jacknicholson@gmail.com"
    password = "123456789"

    @classmethod
    def setUpClass(cls):
        cls.driver.maximize_window()
        shopcart = MyAccountNinja(cls.driver)
        cls.driver.get(shopcart.url)
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_my_account_02_ninja(self):
        myacc = MyAccountNinja(self.driver)

        # Click on "My Account" link
        myacc.click_my_account_link()

        # Click on "Login" link
        myacc.click_login_link()

        # Enter a valid email address
        myacc.set_email(self.email_address)

        # Enter a valid password
        myacc.set_password(self.password)

        # Click on "Login" button
        myacc.click_login_button()

        # Check if all links under "My Orders" text are displayed
        element = self.driver.find_element_by_xpath(MyAccountNinja.order_history_link).is_displayed()
        if element:
            print("OK. 'Order History' link is displayed.")
        else:
            sys.exit("ERROR. 'Order History' link is not displayed.")

        element = self.driver.find_element_by_xpath(MyAccountNinja.downloads_link).is_displayed()
        if element:
            print("OK. 'Downloads' link is displayed.")
        else:
            sys.exit("ERROR. 'Downloads' link is not displayed.")

        element = self.driver.find_element_by_xpath(MyAccountNinja.reward_points_link).is_displayed()
        if element:
            print("OK. 'Reward Points' link is displayed.")
        else:
            sys.exit("ERROR. 'Reward Points' link is not displayed.")

        element = self.driver.find_element_by_xpath(MyAccountNinja.returns_link).is_displayed()
        if element:
            print("OK. 'Returns' link is displayed.")
        else:
            sys.exit("ERROR. 'Returns' link is not displayed.")

        element = self.driver.find_element_by_xpath(MyAccountNinja.transactions_link).is_displayed()
        if element:
            print("OK. 'Transactions' link is displayed.")
        else:
            sys.exit("ERROR. 'Transactions' link is not displayed.")

        element = self.driver.find_element_by_xpath(MyAccountNinja.payment_profile_link).is_displayed()
        if element:
            print("OK. 'Payment Profile' link is displayed.")
        else:
            sys.exit("ERROR. 'Payment Profile' link is not displayed.")

        myacc.click_order_history_link()
        element = self.driver.find_element_by_xpath(MyAccountNinja.verify_order_history).is_displayed()
        if element:
            print("OK. 'Order History' link is working.")
        else:
            sys.exit("ERROR. 'Order History' link is broken.")
        myacc.click_my_account_link()
        myacc.click_my_account_link_2()

        myacc.click_downloads_link()
        element = self.driver.find_element_by_xpath(MyAccountNinja.verify_downloads).is_displayed()
        if element:
            print("OK. 'Downloads' link is working.")
        else:
            sys.exit("ERROR. 'Downloads' link is broken.")
        myacc.click_my_account_link()
        myacc.click_my_account_link_2()

        myacc.click_reward_points_link()
        element = self.driver.find_element_by_xpath(MyAccountNinja.verify_reward_points).is_displayed()
        if element:
            print("OK. 'Reward Points' link is working.")
        else:
            sys.exit("ERROR. 'Reward Points' link is broken.")
        myacc.click_my_account_link()
        myacc.click_my_account_link_2()

        myacc.click_transactions_link()
        element = self.driver.find_element_by_xpath(MyAccountNinja.verify_transactions).is_displayed()
        if element:
            print("OK. 'Transactions' link is working.")
        else:
            sys.exit("ERROR. ''Transactions' link is broken.")
        myacc.click_my_account_link()
        myacc.click_my_account_link_2()

        myacc.click_payment_profile_link()
        element = self.driver.find_element_by_xpath(MyAccountNinja.verify_payment_profile).is_displayed()
        if element:
            print("OK. 'Payment Profile' link is working.")
        else:
            sys.exit("ERROR. ''Payment Profile' link is broken.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="MyAccountTest02Ninja"))
