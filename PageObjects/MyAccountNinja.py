from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

__author__ = "Chirosca Tudor"
__email__ = "tudorache@gmail.com"


class MyAccountNinja:
    # Locators of all elements
    #    browser = webdriver.Chrome("C:/Users/Tudor/PycharmProjects/Sephora/Drivers/chromedriver.exe")
#    browser = webdriver.Firefox()
    my_account_link = "//*[@class='hidden-xs hidden-sm hidden-md' and text()='My Account']"
    my_account_link_2 = "//*[@id='top-links']/ul/li[2]/ul/li[1]/a"
    login_link = "//a[text()='Login']"
    email_id = "//*[@id='input-email']"
    password_id = "//*[@id='input-password']"
    login_button = "//input[@class='btn btn-primary']"
    edit_account_link = "//*[@id='content']/ul[1]/li[1]/a"
    password_link = "//*[@id='content']/ul[1]/li[2]/a"
    address_book_link = "//*[@id='content']/ul[1]/li[3]/a"
    wish_list_link = "//*[@id='content']/ul[1]/li[4]/a"
    verify_edit_account = "//*[text()='Your Personal Details']"
    verify_password_link = "//legend[text()='Password']"
    verify_address_book = "//h2[text()='Address Book Entries']"
    verify_wish_list = "//a[text()='My Wish List']"
    back_button = "//a[@class='btn btn-default' and text()='Back']"
    order_history_link = "//*[@id='content']/ul[2]/li[1]/a"
    downloads_link = "//*[@id='content']/ul[2]/li[2]/a"
    reward_points_link = "//*[@id='content']/ul[2]/li[3]/a"
    returns_link = "//*[@id='content']/ul[2]/li[4]/a"
    transactions_link = "//*[@id='content']/ul[2]/li[5]/a"
    payment_profile_link = "//*[@id='content']/ul[2]/li[6]/a"
    verify_order_history = "//*[@id='account-order']/ul/li[3]/a"
    verify_downloads = "//*[@id='account-download']/ul/li[3]/a"
    verify_reward_points = "//*[@id='account-reward']/ul/li[3]/a"
    verify_returns = "//*[@id='account-return']/ul/li[3]/a"
    verify_transactions = "//*[@id='account-transaction']/ul/li[3]/a"
    verify_payment_profile = "//*[@id='account-recurring']/ul/li[3]/a"
    reg_aff_acc_link = "//a[text()='Register for an affiliate account']"
    verify_reg_aff_acc = "//legend[text()='My Affiliate Account']"
    newsletter_link = "//*[@id='content']/ul[4]/li/a"
    verify_newsletter = "//*[@id='account-newsletter']/ul/li[3]/a"
    first_name_field = "//input[@name='firstname']"
    verify_first_name = "//*[@id='input-firstname']/@value"
    last_name_field = "//input[@name='lastname']"
    email_field = "//input[@name='email']"
    telephone_field = "//input[@name='telephone']"
    continue_button = "//input[@value='Continue']"
    warning_first_name = "//*[text()='First Name must be between 1 and 32 characters!']"
    warning_last_name = "//*[text()='Last Name must be between 1 and 32 characters!']"
    warning_email = "//*[text()='E-Mail Address does not appear to be valid!']"
    warning_telephone = "//*[text()='Telephone must be between 3 and 32 characters!']"
    new_address_button = "//*[@id='content']/div[2]/div[2]/a"
    new_address_first_name = "//*[@id='input-firstname']"
    new_address_last_name = "//*[@id='input-lastname']"
    new_address_address = "//*[@id='input-address-1']"
    new_address_city = "//*[@id='input-city']"
    new_address_zip = "//*[@id='input-postcode']"
    select_country_id = "input-country"
    country_value = "223"
    select_state_id = "input-zone"
    state_value = "3669"
    verify_new_address = "//*[@id='content']/div[1]/table/tbody/tr[2]/td[1]"
    new_address_delete_button = "//*[@id='content']/div[1]/table/tbody/tr[2]/td[2]/a[2]"
    yes_radio_button = "//*[@id='content']/form/fieldset/div[10]/div/label[1]/input"
    warning_delete_address = "//*[text()=' Warning: You can not delete your default address!']"
    new_address_edit_button = "//*[@id='content']/div[1]/table/tbody/tr[2]/td[2]/a[1]"
    no_radio_button = "//*[@id='content']/form/fieldset/div[10]/div/label[2]/input"

    def __init__(self, driver):
        self.driver = driver
        self.url = "http://tutorialsninja.com/demo/index.php?route=common/home"

    def select_no_radio_button(self):
        ActionChains(self.driver).click(self.driver.find_element_by_xpath(self.no_radio_button)).perform()

    def click_new_address_edit_button(self):
        self.driver.find_element_by_xpath(self.new_address_edit_button).click()

    def select_yes_radio_button(self):
        ActionChains(self.driver).click(self.driver.find_element_by_xpath(self.yes_radio_button)).perform()

    def click_new_address_delete_button(self):
        self.driver.find_element_by_xpath(self.new_address_delete_button).click()

    def set_new_address_first_name(self, new_first_name):
        self.driver.find_element_by_xpath(self.new_address_first_name).clear()
        self.driver.find_element_by_xpath(self.new_address_first_name).send_keys(new_first_name)

    def set_new_address_last_name(self, new_last_name):
        self.driver.find_element_by_xpath(self.new_address_last_name).clear()
        self.driver.find_element_by_xpath(self.new_address_last_name).send_keys(new_last_name)

    def set_new_address(self, new_address):
        self.driver.find_element_by_xpath(self.new_address_address).clear()
        self.driver.find_element_by_xpath(self.new_address_address).send_keys(new_address)

    def set_new_address_city(self, new_city):
        self.driver.find_element_by_xpath(self.new_address_city).clear()
        self.driver.find_element_by_xpath(self.new_address_city).send_keys(new_city)

    def set_new_address_zip(self, new_zip):
        self.driver.find_element_by_xpath(self.new_address_zip).clear()
        self.driver.find_element_by_xpath(self.new_address_zip).send_keys(new_zip)

    def set_country_usa(self):
        dropdown = Select(self.driver.find_element_by_id(self.select_country_id))
        dropdown.select_by_value(self.country_value)

    def set_state_texas(self):
        dropdown = Select(self.driver.find_element_by_id(self.select_state_id))
        dropdown.select_by_value(self.state_value)

    def click_my_account_link(self):
        self.driver.find_element_by_xpath(self.my_account_link).click()

    def click_my_account_link_2(self):
        self.driver.find_element_by_xpath(self.my_account_link_2).click()

    def click_login_link(self):
        self.driver.find_element_by_xpath(self.login_link).click()

    def set_email(self, email):
        self.driver.find_element_by_xpath(self.email_id).clear()
        self.driver.find_element_by_xpath(self.email_id).send_keys(email)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.password_id).clear()
        self.driver.find_element_by_xpath(self.password_id).send_keys(password)

    def click_login_button(self):
        self.driver.find_element_by_xpath(self.login_button).click()

    def click_edit_account_link(self):
        self.driver.find_element_by_xpath(self.edit_account_link).click()

    def click_password_link(self):
        self.driver.find_element_by_xpath(self.password_link).click()

    def click_address_book_link(self):
        self.driver.find_element_by_xpath(self.address_book_link).click()

    def click_wish_list_link(self):
        self.driver.find_element_by_xpath(self.wish_list_link).click()

    def click_back_button(self):
        self.driver.find_element_by_xpath(self.back_button).click()

    def click_order_history_link(self):
        self.driver.find_element_by_xpath(self.order_history_link).click()

    def click_downloads_link(self):
        self.driver.find_element_by_xpath(self.downloads_link).click()

    def click_reward_points_link(self):
        self.driver.find_element_by_xpath(self.reward_points_link).click()

    def click_returns_link(self):
        self.driver.find_element_by_xpath(self.returns_link).click()

    def click_transactions_link(self):
        self.driver.find_element_by_xpath(self.transactions_link).click()

    def click_payment_profile_link(self):
        self.driver.find_element_by_xpath(self.payment_profile_link).click()

    def click_reg_aff_acc_link(self):
        self.driver.find_element_by_xpath(self.reg_aff_acc_link).click()

    def click_newsletter_link(self):
        self.driver.find_element_by_xpath(self.newsletter_link).click()

    def set_first_name(self, first_name_empty):
        self.driver.find_element_by_xpath(self.first_name_field).clear()
        self.driver.find_element_by_xpath(self.first_name_field).send_keys(first_name_empty)

    def set_last_name(self, last_name_empty):
        self.driver.find_element_by_xpath(self.last_name_field).clear()
        self.driver.find_element_by_xpath(self.last_name_field).send_keys(last_name_empty)

    def set_new_email(self, new_email):
        self.driver.find_element_by_xpath(self.email_field).clear()
        self.driver.find_element_by_xpath(self.email_field).send_keys(new_email)

    def set_telephone(self, telephone_empty):
        self.driver.find_element_by_xpath(self.telephone_field).clear()
        self.driver.find_element_by_xpath(self.telephone_field).send_keys(telephone_empty)

    def click_continue_button(self):
        self.driver.find_element_by_xpath(self.continue_button).click()

    def click_new_address_button(self):
        self.driver.find_element_by_xpath(self.new_address_button).click()







