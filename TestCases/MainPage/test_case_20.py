import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common import action_chains
from PageObjects.MainPage import MainPage
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class MainPageTest20(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        main = MainPage(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get(main.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_mainpage_20(self):
        main = MainPage(self.driver)
        main.click_close_x_icon()

        shop = self.driver.find_element_by_xpath(MainPage.mouseover_shop)
        actions = action_chains.ActionChains(self.driver)
        actions.move_to_element(shop).perform()
        gifts_link = self.driver.find_element_by_xpath(MainPage.gifts_link)
        actions.move_to_element(gifts_link).perform()
        gifts_link.click()
        if self.driver.title == "Best Beauty Gifts in 2019 | Sephora":
            print("OK. Best Beauty Gifts page was opened.")
        else:
            sys.exit("ERROR. Best Beauty Gifts page wasn't opened.")

        main.click_main_page()

        shop = self.driver.find_element_by_xpath(MainPage.mouseover_shop)
        sale_link = self.driver.find_element_by_xpath(MainPage.sale_link)
        actions = action_chains.ActionChains(self.driver)
        actions.move_to_element(shop).perform()
        actions.move_to_element(sale_link).perform()
        sale_link.click()
        if self.driver.title == "Makeup Sale | Beauty Sale | Sephora":
            print("OK. Makeup Sale | Beauty Sale page was opened.")
        else:
            sys.exit("ERROR. Makeup Sale | Beauty Sale page wasn't opened.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="MainPageTest20"))
