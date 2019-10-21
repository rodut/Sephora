import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common import action_chains
from PageObjects.MainPage import MainPage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class MainPageTest17(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        main = MainPage(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get(main.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_mainpage_17(self):
        wait = WebDriverWait(self.driver, 10)
        main = MainPage(self.driver)
        main.click_close_x_icon()
        # Mouseover "SHOP" dropdown box
        # Click on "MAKEUP" link box
        shop = self.driver.find_element_by_xpath(MainPage.mouseover_shop)
        makeup = self.driver.find_element_by_xpath(MainPage.makeup_link)
        actions = action_chains.ActionChains(self.driver)
        actions.move_to_element(shop).perform()
        actions.move_to_element(makeup).perform()
        makeup.click()
#        actions.move_to_element(shop).move_to_element(makeup).click().perform()
        # Verify if the right page was opened
        if self.driver.title == "Makeup | Sephora":
            print("OK. Makeup page was opened.")
        else:
            sys.exit("ERROR. Makeup page wasn't opened.")
        # Go back to the main page
        main.click_main_page()
        # Mouseover "SHOP" dropdown box
        # Click "SKINCARE" link box
        shop = self.driver.find_element_by_xpath(MainPage.mouseover_shop)
        skincare = self.driver.find_element_by_xpath(MainPage.skincare_link)
        actions = action_chains.ActionChains(self.driver)
        actions.move_to_element(shop).perform()
        actions.move_to_element(skincare).perform()
        skincare.click()
        # Verify if the right page was opened
        if self.driver.title == "Skincare Products | Sephora":
            print("OK. Skincare page was opened.")
        else:
            sys.exit("ERROR. Skincare page wasn't opened.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="MainPageTest17"))
