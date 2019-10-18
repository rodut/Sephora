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


class MainPageTest16(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        main = MainPage(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get(main.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_mainpage_16(self):
        wait = WebDriverWait(self.driver, 10)
        main = MainPage(self.driver)
        main.click_close_x_icon()

        # Click on "Terms of Use" (bottom of the page)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, MainPage.terms_use_link)))
        element.click()

        # Verify if the right page was opened
        element = wait.until(EC.presence_of_all_elements_located((By.XPATH, MainPage.verify_terms_use)))
        if len(element) > 0:
            print("OK. Sephora's Instagram page was opened.")
        else:
            sys.exit("ERROR. Sephora's Instagram page wasn't opened.")

        # Click back button on browser
        main.browser_back_button()

        # Click on "Privacy Policy" link
        element = wait.until(EC.element_to_be_clickable((By.XPATH, MainPage.privacy_policy_link)))
        element.click()

        # Verify if the right page was opened
        element = wait.until(EC.presence_of_all_elements_located((By.XPATH, MainPage.verify_privacy_policy)))
        if len(element) > 0:
            print("OK. Sephoria's Youtube page was opened.")
        else:
            sys.exit("ERROR. Sephoria's Youtube page wasn't opened.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="MainPageTest16"))
