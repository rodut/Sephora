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
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_register_015(self):
        reg = Register(self.driver)
        reg.close_icon()
        reg.click_register()
        reg.click_terms()
        time.sleep(3)
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        time.sleep(1)
        print(self.driver.title)
        if self.driver.title == "Google Terms of Service – Privacy & Terms – Google":
            print("OK. User can see 'Google Terms of Service' page.")
        else:
            sys.exit("ERROR. User cannot see 'Google Terms of Service' page.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="RegisterTest015"))


'''
            
                for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            print(self.driver.title)
        if self.driver.title == "Privacy Policy – Privacy & Terms – Google":
            print("OK. User can see 'Google Privacy Policy' page.")
        else:
            sys.exit("ERROR. User cannot see 'Google Privacy Policy' page.")
'''