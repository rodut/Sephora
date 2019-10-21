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


class MainPageTest26(unittest.TestCase):
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

    def test_mainpage_26(self):
        wait = WebDriverWait(self.driver, 10)
        main = MainPage(self.driver)
        main.click_close_x_icon()
        # In the search bar type "shaving" and hit enter
        main.set_site_search(self.search_item)
        # Click on any category name, ex. "Skincare (16)"
        element = self.driver.find_element_by_xpath(MainPage.verify_skincare_1)
        x = element.text
        y = x.replace("Skincare (", "")
        z = y.replace(")", "")
        skin_n1 = int(z)
        main.click_skincare_link()
        # Scroll down the page
        main.scroll_down_page_lights()
        # Check to see if the number next to the category matches the number of products displayed (16)
        element = wait.until(EC.presence_of_all_elements_located((By.XPATH, MainPage.verify_skincare_2)))
        if len(element) == skin_n1:
            print("OK. User can view only that particular category.")
        else:
            sys.exit("ERROR. User can view only that particular category.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="MainPageTest26"))
