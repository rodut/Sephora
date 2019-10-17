from selenium import webdriver

__author__ = "Chirosca Tudor"
__email__ = "tudorache@gmail.com"


class RegisterNinja:
    # Locators of all elements
#    browser = webdriver.Chrome("C:/Users/Tudor/PycharmProjects/Sephora/Drivers/chromedriver.exe")
#    browser = webdriver.Firefox()
    my_account_link = "//*[@class='hidden-xs hidden-sm hidden-md' and text()='My Account']"
    register_link = "//*[text()='Register']"
    first_name_id = "//*[@id='input-firstname']"
    last_name_id = "//*[@id='input-lastname']"
    email_id = "//*[@id='input-email']"
    telephone_id = "//*[@id='input-telephone']"
    password_id = "//*[@id='input-password']"
    password_confirm_id = "//*[@id='input-confirm']"
    privacy_policy_checkbox_name = "//input[@name='agree']"
    continue_button = "//*[@class='btn btn-primary']"
    success_link = "//a[text()='Success']"
    continue_button_2 = "//*[@class='btn btn-primary']"
    account_link = "//*[text()='Account']"
    warning_email = "//*[@class='alert alert-danger alert-dismissible']"

    def __init__(self, driver):
        self.driver = driver
        self.url = "http://tutorialsninja.com/demo/index.php?route=common/home"

    def click_my_account_link(self):
        self.driver.find_element_by_xpath(self.my_account_link).click()

    def click_register_link(self):
        self.driver.find_element_by_xpath(self.register_link).click()

    def set_first_name(self, first_name):
        self.driver.find_element_by_xpath(self.first_name_id).clear()
        self.driver.find_element_by_xpath(self.first_name_id).send_keys(first_name)

    def set_last_name(self, last_name):
        self.driver.find_element_by_xpath(self.last_name_id).clear()
        self.driver.find_element_by_xpath(self.last_name_id).send_keys(last_name)

    def set_email(self, email):
        self.driver.find_element_by_xpath(self.email_id).clear()
        self.driver.find_element_by_xpath(self.email_id).send_keys(email)

    def set_telephone(self, telephone):
        self.driver.find_element_by_xpath(self.telephone_id).clear()
        self.driver.find_element_by_xpath(self.telephone_id).send_keys(telephone)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.password_id).clear()
        self.driver.find_element_by_xpath(self.password_id).send_keys(password)

    def set_password_confirm(self, password_confirm):
        self.driver.find_element_by_xpath(self.password_confirm_id).clear()
        self.driver.find_element_by_xpath(self.password_confirm_id).send_keys(password_confirm)

    def click_privacy_policy_checkbox(self):
        self.driver.find_element_by_xpath(self.privacy_policy_checkbox_name).click()

    def click_continue_button(self):
        self.driver.find_element_by_xpath(self.continue_button).click()

    def click_continue_button_2(self):
        self.driver.find_element_by_xpath(self.continue_button_2).click()


