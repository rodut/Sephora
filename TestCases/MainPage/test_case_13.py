import unittest
import HtmlTestRunner
from PageObjects.MainPage import MainPage
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class MainPageTest13(unittest.TestCase):
    driver = webdriver.Chrome()
    @classmethod
    def setUpClass(cls):
        main = MainPage(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get(main.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_mainpage_13(self):
        wait = WebDriverWait(self.driver, 10)
        main = MainPage(self.driver)
        main.click_close_x_icon()
        # Click on "Sephora Global Sites" link (bottom of the page)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, MainPage.sephora_global_link)))
        element.click()
        # Verify if the right page was opened
        element = wait.until(EC.presence_of_element_located((By.XPATH, MainPage.verify_sephora_global)))
        assert element.is_displayed(), "ERROR. 'Sephora Global Sites' page wasn't opened."
        # Click back button on browser
        main.browser_back_button()
        # Click on "Sephoria" link (bottom of the page)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, MainPage.sephoria_link)))
        element.click()
        time.sleep(1)
        # Go to next windows, and verify if the right page was opened
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        assert self.driver.title == "Sephoria House of Beauty | Buy Your Tickets Here!", "ERROR. 'Sephoria' page wasn't opened."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="MainPageTest13"))
