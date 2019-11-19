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
__email__ = "tudorache@gmail.com"


class MainPageTest14(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        main = MainPage(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get(main.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_mainpage_14(self):
        wait = WebDriverWait(self.driver, 10)
        main = MainPage(self.driver)
        main.click_close_x_icon()
        # Click on facebook icon (bottom of the page)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, MainPage.facebook_icon)))
        element.click()
        # Check if the Sefora's facebook page was opened
        element = wait.until(EC.presence_of_element_located((By.XPATH, MainPage.verify_facebook)))
        assert element.is_displayed(), "ERROR. Sephora's Facebook page wasn't opened."
        # Click back button on browser
        main.browser_back_button()
        # Click on twitter icon (bottom of the page)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, MainPage.twitter_icon)))
        element.click()
        # Check if the Sefora's twitter page opened
        wait.until(EC.presence_of_element_located((By.XPATH, MainPage.verify_twitter)))
        assert self.driver.title == "Sephora (@Sephora) | Twitter", "ERROR. Sephoria's Twitter page wasn't opened."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="MainPageTest14"))
