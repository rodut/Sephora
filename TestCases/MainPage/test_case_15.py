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


class MainPageTest15(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        main = MainPage(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get(main.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_mainpage_15(self):
        wait = WebDriverWait(self.driver, 10)
        main = MainPage(self.driver)
        main.click_close_x_icon()

        element = wait.until(EC.element_to_be_clickable((By.XPATH, MainPage.instagram_icon)))
        element.click()
        element = wait.until(EC.presence_of_all_elements_located((By.XPATH, MainPage.verify_instagram)))
        if len(element) > 0:
            print("OK. Sephora's Instagram page was opened.")
        else:
            sys.exit("ERROR. Sephora's Instagram page wasn't opened.")

        # Click back button on browser
        main.browser_back_button()

        element = wait.until(EC.element_to_be_clickable((By.XPATH, MainPage.youtube_icon)))
        element.click()
        element = wait.until(EC.presence_of_all_elements_located((By.XPATH, MainPage.verify_youtube)))
        if len(element) > 0:
            print("OK. Sephoria's Youtube page was opened.")
        else:
            sys.exit("ERROR. Sephoria's Youtube page wasn't opened.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="MainPageTest15"))
