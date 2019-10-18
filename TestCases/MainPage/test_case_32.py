import unittest
import HtmlTestRunner
from selenium import webdriver
from PageObjects.MainPage import MainPage
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class MainPageTest32(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        main = MainPage(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get(main.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_mainpage_32(self):
        wait = WebDriverWait(self.driver, 10)
        main = MainPage(self.driver)
        main.click_close_x_icon()

        # Mouseover "GIFTS" dropdown box
        gifts = self.driver.find_element_by_xpath(MainPage.mouseover_gifts)
        gifts.click()

        # Click on "View All Gifts"
        view_all_gifts = self.driver.find_element_by_xpath(MainPage.view_all_gifts)
        view_all_gifts.click()

        # In "Filter by:" select "CLINIQUE" checkbox
        checkbox = self.driver.find_element_by_xpath(MainPage.clinique_checkbox)
        ActionChains(self.driver).click(checkbox).perform()

        # Scroll down to the bottom of the page
        main.scroll_bottom_page()

        # Verify if all the products names matches the selected "CLINIQUE" checkbox
        element = self.driver.find_element_by_xpath(MainPage.verify_clinique)
        if element.text == "CLINIQUE":
            print("OK. All products displayed are Clinique's.")
        else:
            sys.exit("ERROR. Not all products are Clinique's.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="MainPageTest32"))
