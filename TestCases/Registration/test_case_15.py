import unittest
import time
import HtmlTestRunner
from selenium import webdriver
from PageObjects.Register import Register
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class RegisterTest015(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        reg = Register(cls.driver)
        cls.driver.get(reg.url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_register_15(self):
        reg = Register(self.driver)
        reg.close_icon()
        # Click on "Register" link
        reg.click_register()
        # Click "terms" link
        reg.click_terms()
        time.sleep(1)
        # Switch to new opened window
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        time.sleep(1)
        print(self.driver.title)
        # Verify if "terms" link was opened
        assert self.driver.title == "Google Terms of Service – Privacy & Terms – Google", "ERROR. User cannot see 'Google Terms of Service' page."



if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="RegisterTest15"))
