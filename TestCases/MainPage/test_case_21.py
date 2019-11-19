import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from PageObjects.MainPage import MainPage
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class MainPageTest21(unittest.TestCase):
    driver = webdriver.Chrome()
    search_item = "perfume"

    @classmethod
    def setUpClass(cls):
        main = MainPage(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get(main.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_mainpage_21(self):
        wait = WebDriverWait(self.driver, 10)
        main = MainPage(self.driver)
        main.click_close_x_icon()
        # In the search bar type "perfume" than hit enter
        main.set_site_search(self.search_item)
        # Scroll down the page
        main.scroll_down_page()
        # Verify if all the products on the first page of the search result are "perfume"
        element = wait.until(EC.presence_of_all_elements_located((By.XPATH, MainPage.search_result)))
        assert len(element) == 60, "ERROR. There are more/less than 60 products on the first page result."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="MainPageTest21"))
