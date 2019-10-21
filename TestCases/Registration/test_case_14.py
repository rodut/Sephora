import unittest
import time
import HtmlTestRunner
from selenium import webdriver
from PageObjects.Register import Register
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class RegisterTest014(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        reg = Register(cls.driver)
        cls.driver.get(reg.url)
        cls.driver.maximize_window()
        time.sleep(1)

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
        time.sleep(3)
        # Switch to new opened window
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        time.sleep(1)
        print(self.driver.title)
        # Verify if "privacy policy" link was opened
        if self.driver.title == "Privacy Policy – Privacy & Terms – Google":
            print("OK. User can see 'Google Privacy Policy' page.")
        else:
            sys.exit("ERROR. User cannot see 'Google Privacy Policy' page.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="RegisterTest14"))
