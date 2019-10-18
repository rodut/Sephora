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


class MainPageTest29(unittest.TestCase):
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

    def test_mainpage_29(self):
        wait = WebDriverWait(self.driver, 10)
        main = MainPage(self.driver)
        main.click_close_x_icon()

        # In the search bar type "shaving" and hit enter
        main.set_site_search(self.search_item)

        # Click "Sort by:" and select "Brand Name"
        main.click_dropdown_sort_by()
        main.click_brand_name_link()

        # Verify if all the brands are arranged in alphabetical order
        element = wait.until(EC.presence_of_element_located((By.XPATH, MainPage.verify_brand_name)))
        if element:
            print("OK. Products are sorted by Brand Name.")
        else:
            sys.exit("ERROR. Products are not sorted by Brand Name.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="MainPageTest29"))
