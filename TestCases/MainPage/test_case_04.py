import unittest
import HtmlTestRunner
from PageObjects.MainPage import MainPage
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"


class MainPageTest04(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        main = MainPage(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get(main.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_mainpage_04(self):
        wait = WebDriverWait(self.driver, 10)
        main = MainPage(self.driver)
        # Click on "Find a Store" link
        main.click_close_x_icon()
        main.click_find_store_link()
        # Check if page changed to "Find a Sephora", if no => ERROR
        element = wait.until(EC.presence_of_element_located((By.XPATH, MainPage.verify_find_store)))
        assert element.is_displayed(), "ERROR. Page did not changed to 'Find a Sephora'."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="MainPageTest04"))
