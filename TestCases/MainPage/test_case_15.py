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
        # Click on instagram icon (bottom of the page)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, MainPage.instagram_icon)))
        element.click()
        # Check if the Sefora's instagram page was opened
        element = wait.until(EC.presence_of_element_located((By.XPATH, MainPage.verify_instagram)))
        assert element.is_displayed(), "ERROR. Sephora's Instagram page wasn't opened."
        # Click back button on browser
        main.browser_back_button()
        # Click on youtube icon (bottom of the page)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, MainPage.youtube_icon)))
        element.click()
        # Check if the Sefora's youtube page was opened
        wait.until(EC.presence_of_element_located((By.XPATH, MainPage.verify_youtube)))
        assert self.driver.title == "Sephora - YouTube", "ERROR. Sephoria's Youtube page wasn't opened."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="MainPageTest15"))
