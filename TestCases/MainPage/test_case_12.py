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


class MainPageTest12(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        main = MainPage(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get(main.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_mainpage_12(self):
        wait = WebDriverWait(self.driver, 10)
        main = MainPage(self.driver)
        main.click_close_x_icon()
        # Click on "Affiliates" link (bottom of the page)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, MainPage.affiliates_link)))
        element.click()
        # Verify if the right page was opened
        element = wait.until(EC.presence_of_element_located((By.XPATH, MainPage.verify_affiliates)))
        assert element.is_displayed(), "ERROR. 'Affiliates' page wasn't opened."
        # Click back button on browser
        main.browser_back_button()
        # Click on "Supply Chain Transparency" link (bottom of the page)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, MainPage.supply_chain_link)))
        element.click()
        # Verify if the right page was opened
        element = wait.until(EC.presence_of_element_located((By.XPATH, MainPage.verify_supply_chain)))
        assert element.is_displayed(), "ERROR. 'Supply Chain Transparency' page wasn't opened."
        # Click back button on browser
        main.browser_back_button()
        # Click on "Sitemap" link (bottom of the page)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, MainPage.sitemap_link)))
        element.click()
        # Verify if the right page was opened
        element = wait.until(EC.presence_of_element_located((By.XPATH, MainPage.verify_sitemap)))
        assert element.is_displayed(), "ERROR. 'Sitemap' page wasn't opened."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="MainPageTest12"))
