import unittest
import HtmlTestRunner
from selenium import webdriver
from PageObjects.MainPage import MainPage
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class MainPageTest30(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        main = MainPage(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get(main.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_mainpage_30(self):
        main = MainPage(self.driver)
        main.click_close_x_icon()
        # Mouseover "GIFTS" dropdown box
        gifts = self.driver.find_element_by_xpath(MainPage.mouseover_gifts)
        gifts.click()
        # Select "$10 and Under"
        ten_and_under = self.driver.find_element_by_xpath(MainPage.ten_and_under)
        ten_and_under.click()
        # Verify if all products are under or equal to $10
        prices = self.driver.find_elements_by_xpath(MainPage.prices_under_ten)
        for price in prices:
            x = price.text
            g = x.replace(".50", "")
            y = g.replace(".00", "")
            k = y.replace("$", "")
            print(int(k))
            assert int(k) <= 10, "ERROR. There are prices greater than $10."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="MainPageTest30"))
