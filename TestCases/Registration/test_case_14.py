import unittest
import time
import HtmlTestRunner
from selenium import webdriver
from PageObjects.Register import Register
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"


class RegisterTest014(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        reg = Register(cls.driver)
        cls.driver.get(reg.url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_register_14(self):
        reg = Register(self.driver)
        reg.close_icon()
        # Click "Register" link
        reg.click_register()
        # Click on "Privacy Policy" link
        reg.click_privacy_policy()
        time.sleep(1)
        # Switch to new opened window
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        time.sleep(1)
        # Verify if "privacy policy" link was opened
        assert self.driver.title == "Privacy Policy – Privacy & Terms – Google", "ERROR. User cannot see 'Google Privacy Policy' page."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="RegisterTest14"))
