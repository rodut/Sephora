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


class MainPageTest28(unittest.TestCase):
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

    def test_mainpage_28(self):
        wait = WebDriverWait(self.driver, 10)
        main = MainPage(self.driver)
        main.click_close_x_icon()
        # In the search bar type "shaving" and hit enter
        main.set_site_search(self.search_item)
        products_nr = self.driver.find_element_by_xpath(MainPage.number_of_products)
        a = products_nr.text
        number = a.replace(" Product results", "")
        # Scroll down the page
        main.scroll_bottom_page()
        # In the bottom of the page select page 2
        element1 = wait.until(EC.presence_of_all_elements_located((By.XPATH, MainPage.verify_skincare_2)))
        first_page_products = len(element1)
        page_2 = self.driver.find_element_by_xpath(MainPage.click_page_2)
        page_2.click()
        # Scroll to the bottom of the page
        main.scroll_bottom_page()
        # Check if the number next to "Product results: 'shaving'" matches to the number of products displayed on the both pages
        element2 = wait.until(EC.presence_of_all_elements_located((By.XPATH, MainPage.verify_skincare_2)))
        second_page_products = len(element2)
        all_products = first_page_products + second_page_products
        assert int(number) == all_products, "ERROR. The number next to 'Product results: shaving' doesn't match to the number of products displayed."

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="MainPageTest28"))
