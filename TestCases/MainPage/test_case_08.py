import unittest
import HtmlTestRunner
from PageObjects.MainPage import MainPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class MainPageTest08(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        main = MainPage(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get(main.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_mainpage_08(self):
        wait = WebDriverWait(self.driver, 10)
        main = MainPage(self.driver)
        main.click_close_x_icon()

        # Check if there are 18 products under "Recommended For You", if no => ERROR
        element = wait.until(EC.presence_of_all_elements_located((By.XPATH, MainPage.recommended_items)))
        if len(element) == 18:
            print("OK. There are 18 products under 'Recommended For You'.")
        else:
            sys.exit("ERROR. There are more/less than 18 products under 'Recommended For You'.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="MainPageTest08"))
