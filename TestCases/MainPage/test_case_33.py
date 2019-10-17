import unittest
import HtmlTestRunner
from selenium import webdriver
from PageObjects.MainPage import MainPage
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class MainPageTest33(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        main = MainPage(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get(main.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_mainpage_33(self):
        main = MainPage(self.driver)
        main.click_close_x_icon()

        new = self.driver.find_element_by_xpath(MainPage.mouseover_new)
        new.click()
        main.scroll_down_page()
        main.scroll_down_page()
        main.scroll_down_page()
        main.scroll_down_page()
        main.scroll_down_page()
        main.scroll_down_page()
        element = self.driver.find_element_by_xpath(MainPage.verify_new)
        if element.text == "NEW":
            print("OK. All products displayed are 'New'.")
        else:
            sys.exit("ERROR. Not all the products are 'New'.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="MainPageTest33"))
