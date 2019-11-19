import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common import action_chains
from PageObjects.MainPage import MainPage
from selenium.webdriver.support.wait import WebDriverWait
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class MainPageTest31(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        main = MainPage(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get(main.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_mainpage_31(self):
        main = MainPage(self.driver)
        main.click_close_x_icon()
        # Mouseover "GIFTS" dropdown box
        brands = self.driver.find_element_by_xpath(MainPage.mouseover_brands)
        actions = action_chains.ActionChains(self.driver)
        actions.move_to_element(brands).perform()
        # Click on "Brands A-Z"
        brands_az = self.driver.find_element_by_xpath(MainPage.brands_a_z)
        brands_az.click()
        # Click on brand name "Dior"
        dior = self.driver.find_element_by_xpath(MainPage.brand_dior)
        dior.click()
        # Scroll down to the bottom of the page
        main.scroll_bottom_page()
        # Verify if only "Dior" products are displayed
        element = self.driver.find_element_by_xpath(MainPage.verify_dior)
        assert element.text == "DIOR", "ERROR. Not all products are Dior's."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="MainPageTest31"))
