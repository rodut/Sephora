import unittest
import HtmlTestRunner
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from PageObjects.MainPage import MainPage
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"


class MainPageTest24(unittest.TestCase):
    driver = webdriver.Chrome()
    search_item = "shaving"

    @classmethod
    def setUpClass(cls):
        main = MainPage(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get(main.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_mainpage_24(self):
        main = MainPage(self.driver)
        main.click_close_x_icon()
        # In the search bar type "shaving" and hit enter
        main.set_site_search(self.search_item)
        # Adjust "Price Range" from $50 to $150
        main.set_sliders()
        # Scroll down the page
        main.scroll_down_page()
        # Verify if user can view only the products with the price between $50 and $150
        prices = self.driver.find_elements_by_xpath(MainPage.prices_50_150)
        for price in prices:
            x = price.text
            y = x.replace(".00", "")
            k = y.replace("$", "")
            q = k.replace("58 - ", "")
            z = q.replace("28 - ", "")
            w = int(z)
            if 50 <= w <= 150:
                print("OK. The products are in range between $50 and $150.")
            else:
                sys.exit("ERROR. The products are not in range between $50 and $150.")
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(1)
        # Click on "Reset all filters"
        main.click_reset_filters()
        time.sleep(1)
        # Verify if user can view all the products with price between 50-150 and other
        prices = self.driver.find_elements_by_xpath(MainPage.prices_50_150)
        for price in prices:
            x = price.text
#            y = x.replace(".00", "")
            k = x.replace("$", "")
            z = k.replace(" - ", "\n")
            w = float(z)
            if 5.00 <= w <= 160.00:
                print("OK. The products are in range between $5 and $160.")
            else:
                sys.exit("ERROR. The products are not in range between $5 and $160.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="MainPageTest24"))
