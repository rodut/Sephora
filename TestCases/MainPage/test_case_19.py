import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common import action_chains
from PageObjects.MainPage import MainPage
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class MainPageTest19(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        main = MainPage(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get(main.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_mainpage_19(self):
        main = MainPage(self.driver)
        main.click_close_x_icon()

        shop = self.driver.find_element_by_xpath(MainPage.mouseover_shop)
        actions = action_chains.ActionChains(self.driver)
        actions.move_to_element(shop).perform()
        fragrance = self.driver.find_element_by_xpath(MainPage.fragrance_link)
        actions.move_to_element(fragrance).perform()
        fragrance.click()
#        actions.move_to_element(shop).move_to_element(makeup).click().perform()
        if self.driver.title == "Fragrance | Sephora":
            print("OK. Fragrance page was opened.")
        else:
            sys.exit("ERROR. Fragrance page wasn't opened.")

        main.click_main_page()

        shop = self.driver.find_element_by_xpath(MainPage.mouseover_shop)
        bath_body = self.driver.find_element_by_xpath(MainPage.bath_body_link)
        actions = action_chains.ActionChains(self.driver)
        actions.move_to_element(shop).perform()
        actions.move_to_element(bath_body).perform()
        bath_body.click()
        if self.driver.title == "Bath Products & Body Products | Sephora":
            print("OK. Bath Products & Body Products page was opened.")
        else:
            sys.exit("ERROR. Bath Products & Body Products page wasn't opened.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="MainPageTest19"))
