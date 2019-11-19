
import unittest
import HtmlTestRunner
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from PageObjects.MainPage import MainPage
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class MainPageTest25(unittest.TestCase):
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

    def test_mainpage_25(self):
        wait = WebDriverWait(self.driver, 10)
        main = MainPage(self.driver)
        main.click_close_x_icon()
        # In the search bar type "shaving" and hit enter
        main.set_site_search(self.search_item)
        # From "Sort by:" select "Price Low to High"
        main.click_dropdown_sort_by()
        main.click_price_low_high()
        # Verify if all the prices are listed correctly, from low to high
        element = wait.until(EC.presence_of_element_located((By.XPATH, MainPage.verify_low_high)))
        assert element, "ERROR. Products are not selected from low to high."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="MainPageTest25"))
