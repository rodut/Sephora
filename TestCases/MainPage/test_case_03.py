import unittest
import HtmlTestRunner
import time
from PageObjects.MainPage import MainPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class MainPageTest03(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = MainPage.browser
        main = MainPage(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get(main.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver = MainPage.browser
        cls.driver.quit()

    def test_mainpage_03(self):
        wait = WebDriverWait(self.driver, 10)
        main = MainPage(self.driver)
        main.click_close_x_icon()
        main.click_track_order_link()
        element = wait.until(EC.presence_of_element_located((By.XPATH, MainPage.verify_track_order)))
        if element:
            print("OK. Page changed to 'ORDER STATUS & HISTORY'.")
        else:
            sys.exit("ERROR. Page did not changed to 'ORDER STATUS & HISTORY'.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="MainPageTest03"))
