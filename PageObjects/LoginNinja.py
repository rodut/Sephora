from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

__author__ = "Chirosca Tudor"
__email__ = "tudorache@gmail.com"


class LoginNinja:
    # Locators of all elements
#    browser = webdriver.Chrome("C:/Users/Tudor/PycharmProjects/Sephora/Drivers/chromedriver.exe")
#    browser = webdriver.Firefox()
    my_account_link = "//*[@class='hidden-xs hidden-sm hidden-md' and text()='My Account']"
    login_link = "//a[text()='Login']"
    email_id = "//*[@id='input-email']"
    password_id = "//*[@id='input-password']"
    login_button = "//input[@class='btn btn-primary']"
    warning_message = "//*[@class='alert alert-danger alert-dismissible']"
    logout_link = "//*[@class='list-group-item' and text()='Logout']"
    edit_account_link = "//*[@id='content']/ul[1]/li[1]/a"
    new_customer_text = "//*[@id='content']/div/div[1]/div/h2"
    password_link = "//*[@id='content']/ul[1]/li[2]/a"
    password_confirm = "//*[@id='input-confirm']"
    check_sign_out = "//a[@class='btn btn-primary']"
    forgotten_password = "//*[@id='content']/div/div[2]/div/form/div[2]/a"
    confirm_message = "//*[@class='alert alert-success alert-dismissible']"

    def __init__(self, driver):
        self.driver = driver
        self.url = "http://tutorialsninja.com/demo/index.php?route=common/home"

    def click_my_account_link(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.my_account_link))).click()

    def click_login_link(self):
        self.driver.find_element_by_xpath(self.login_link).click()

    def set_email(self, email):
        self.driver.find_element_by_xpath(self.email_id).clear()
        self.driver.find_element_by_xpath(self.email_id).send_keys(email)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.password_id).clear()
        self.driver.find_element_by_xpath(self.password_id).send_keys(password)

    def set_new_password(self, new_password):
        self.driver.find_element_by_xpath(self.password_id).clear()
        self.driver.find_element_by_xpath(self.password_id).send_keys(new_password)

    def set_password_confirm(self, password_confirm):
        self.driver.find_element_by_xpath(self.password_confirm).clear()
        self.driver.find_element_by_xpath(self.password_confirm).send_keys(password_confirm)

    def click_login_button(self):
        self.driver.find_element_by_xpath(self.login_button).click()

    def windows_back_page(self):
        self.driver.execute_script("window.history.go(-1)")

    def click_edit_account(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.edit_account_link))).click()

    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout_link).click()

    def verify_password(self):
        self.driver.find_element_by_xpath(self.password_id).clear()
        self.driver.find_element_by_xpath(self.password_id).send_keys(Keys.CONTROL, 'a')
        self.driver.find_element_by_xpath(self.password_id).send_keys(Keys.CONTROL, 'c')
        time.sleep(2)
        self.driver.find_element_by_xpath(self.password_id).send_keys(Keys.DELETE)
        self.driver.find_element_by_xpath(self.password_id).send_keys(Keys.CONTROL, 'v')

    def click_password_link(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.password_link))).click()

    def click_forgotten_password_link(self):
        self.driver.find_element_by_xpath(self.forgotten_password).click()






