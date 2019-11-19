from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import time

__author__ = "Tudor C"


class Login:
    # Locators of all elements
#    browser = webdriver.Chrome("C:/Users/Tudor/PycharmProjects/Sephora/Drivers/chromedriver.exe")
#    browser = webdriver.Remote(command_executor='http://127.0.0.1:4446/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
#    browser = webdriver.Firefox()
    close_x_icon = "//*[@id='modalDialog']/button"
    signin_link = "//*[@data-at='sign_in']"
    yes_pass_selected = "//*[@class='css-cw2gxf Radio-dot']"
    email_address_id = "//*[@id='signin_username']"
    yes_password = "//*[@class='css-u0gadu Radio']"
    no_password = "//*[@class='css-1cxlx9j Radio']"
    password_field = "//*[@id='signin_password']"
    forgot_link = "//*[@class='css-1bjkjfu ']"
    cancel_button = "//button[text()='Cancel']"
    continue_button = "//button[text()='Continue']"
    terms_of_use_link = "//*[@class='css-nlkkp4 ' and text()='Terms of Use']"
    privacy_policy_link = "//*[@class='css-nlkkp4 ' and text()='Privacy Policy']"
    what_email_address = "//*[@id='modalDialog']/div[2]/form/label[1]/span"
    have_sephora_password = "//*[@id='modalDialog']/div[2]/form/label[2]/span"
    have_beauty_text = "//*[@class='css-1lp9uav ']"
    alert_incorrect_email = "//*[@class='css-m0igqx ']"
    alert_incorrect_pass = "//*[@data-at='sign_in_error']"
    alert_no_email_address = "//*[@class='css-m0igqx ']"
    alert_pass_missing = "//*[@class='css-m0igqx ']"
    welcome_text = "//*[@class='css-16eiu3l ']"
    encrypted_password = "//*[@type='password']"
    no_new_to_site = "//*[@class='css-1cxlx9j Radio']"
    register_sephora = "//*[@class='css-do0sr5 ']"
    reset_password = "//*[@class='css-do0sr5 ']"
    check_forgot_email = "//*[@value='sephoramajor@gmail.com']"
    check_invalid_forgot_email = "//*[@value='sephoramajordome3500@gmail.com']"
    send_email_button = "//button[text()='Send Email']"
    alert_send_email = "//*[@class='css-kj0kzd ']"
    check_please_signin = "//*[@class='css-do0sr5 ']"
    check_privacy_policy = "//*[@id='what-our-privacy-policy-covers']"
    close_privacy_policy = "//*[@id='MediaModal']/button"
    check_terms_of_use = "//*[@id='terms-of-use']"
    close_terms_of_use = "//*[@id='MediaModal']/button"

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.sephora.com/"

    def close_icon(self):
        self.driver.find_element_by_xpath(self.close_x_icon).click()

    def click_signin(self):
        self.driver.find_element_by_xpath(self.signin_link).click()

    def set_email_address(self, email_address):
        self.driver.find_element_by_xpath(self.email_address_id).clear()
        self.driver.find_element_by_xpath(self.email_address_id).send_keys(email_address)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.password_field).clear()
        self.driver.find_element_by_xpath(self.password_field).send_keys(password)

    def click_continue(self):
        self.driver.find_element_by_xpath(self.continue_button).click()

    def verify_password(self):
        self.driver.find_element_by_xpath(self.password_field).clear()
        self.driver.find_element_by_xpath(self.password_field).send_keys(Keys.CONTROL, 'a')
        self.driver.find_element_by_xpath(self.password_field).send_keys(Keys.CONTROL, 'c')
        time.sleep(2)
        self.driver.find_element_by_xpath(self.password_field).send_keys(Keys.DELETE)
        self.driver.find_element_by_xpath(self.password_field).send_keys(Keys.CONTROL, 'v')

    def click_new_to_site(self):
        self.driver.find_element_by_xpath(self.no_new_to_site).click()

    def click_forgot_link(self):
        self.driver.find_element_by_xpath(self.forgot_link).click()

    def click_send_email_button(self):
        self.driver.find_element_by_xpath(self.send_email_button).click()

    def click_cancel_button(self):
        self.driver.find_element_by_xpath(self.cancel_button).click()

    def click_privacy_policy(self):
        self.driver.find_element_by_xpath(self.privacy_policy_link).click()

    def click_close_privacy_policy(self):
        self.driver.find_element_by_xpath(self.close_privacy_policy).click()

    def click_terms_of_use(self):
        self.driver.find_element_by_xpath(self.terms_of_use_link).click()

    def click_close_terns_of_use(self):
        self.driver.find_element_by_xpath(self.close_terms_of_use).click()
