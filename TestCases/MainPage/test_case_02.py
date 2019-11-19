import unittest
import HtmlTestRunner
from selenium import webdriver
from PageObjects.MainPage import MainPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"


class MainPageTest02(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        main = MainPage(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get(main.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_mainpage_02(self):
        wait = WebDriverWait(self.driver, 10)
        main = MainPage(self.driver)
        # Click "Reorder" link
        main.click_close_x_icon()
        main.click_reorder_link()
        # Check if page changed to "Purchases", if no => ERROR
        element = wait.until(EC.presence_of_element_located((By.XPATH, MainPage.verify_reorder_link)))
        assert element.is_displayed(), "ERROR. Page did not changed to 'Purchases'."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="MainPageTest02"))
