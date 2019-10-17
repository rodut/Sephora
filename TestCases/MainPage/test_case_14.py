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

        element = wait.until(EC.element_to_be_clickable((By.XPATH, MainPage.facebook_icon)))
        element.click()
        element = wait.until(EC.presence_of_all_elements_located((By.XPATH, MainPage.verify_facebook)))
        if len(element) > 0:
            print("OK. Sephora's Facebook page was opened.")
        else:
            sys.exit("ERROR. Sephora's Facebook page wasn't opened.")

        # Click back button on browser
        main.browser_back_button()

        element = wait.until(EC.element_to_be_clickable((By.XPATH, MainPage.twitter_icon)))
        element.click()
        element = wait.until(EC.presence_of_all_elements_located((By.XPATH, MainPage.verify_twitter)))
        if len(element) > 0:
            print("OK. Sephoria's Twitter page was opened.")
        else:
            sys.exit("ERROR. Sephoria's Twitter page wasn't opened.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="MainPageTest14"))
