from selenium import webdriver

__author__ = "Chirosca Tudor"
__email__ = "tudorache@gmail.com"


class Register:
    # Locators of all elements
#    browser = webdriver.Chrome("C:/Users/Tudor/PycharmProjects/Sephora/Drivers/chromedriver.exe")
#    browser = webdriver.Firefox()
    close_x_icon = "//*[@id='modalDialog']/button"
    register_link = "//*[@data-at='register']"
    first_name_id = "//*[@id='firstName']"
    last_name_id = "//*[@id='lastName']"
    email_address_id = "//*[@id='register_email']"
    password_id = "//*[@id='password']"
    register_button = "//*[@class='css-13nlo6e ']"
    register_eye_icon = "//*[@data-comp='IconEye Icon Box']"
    password_text = "//input[@type='text' and @name='password']"
    password_asterisks = "//input[@type='password' and @name='password']"
    month_id = "//*[@id='biRegMonth']"
    day_id = "//*[@id='biRegDay']"
    year_id = "//*[@id='biRegYear']"
    zip_id = "//*[@id='zipCode']"
    alert_msg_first_name = "//*[@id='modalDialog']/div[2]/form/div[1]/div[1]/div/p"
    alert_msg_last_name = "//*[@id='modalDialog']/div[2]/form/div[1]/div[2]/div/p"
    alert_msg_email_address = "//*[@id='modalDialog']/div[2]/form/div[2]/p"
    alert_msg_password = "//*[@id='modalDialog']/div[2]/form/div[3]/div/div/div/p"
    alert_acc_exists = "//*[@class='css-kj0kzd ']"
    alert_incorrect_email = "//*[@class='css-m0igqx ']"
    subscribe_emails = "//*[@name='subscribeSephoraEmail']"
    password_type = "//input[@type='password']"
    terms_conditions = "//button[@class='css-41z7ik ']"
    terms_conditions_verification = "//h2[text()='Beauty Insider Terms & Conditions']"
    privacy_policy = "//a[text()='privacy policy']"
    google_privacy_policy = "//h1[@class='Raglmc' and text()='Privacy Policy']"
    terms = "//a[text()='terms']"
    yes_join_sephora = "//*[@class='css-181pqmg Checkbox-box']"
    subscribe_emails_disabled = "//*[@class='css-164ulp8 Checkbox-box']"
    alert_birth_date = "//*[@class='css-y9wxk1 ']"
    zip_code = "//input[@name='zipCode']"
    alert_zip_code = "//*[@class='css-kj0kzd ']"

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.sephora.com/"

    def close_icon(self):
        self.driver.find_element_by_xpath(self.close_x_icon).click()

    def click_register(self):
        self.driver.find_element_by_xpath(self.register_link).click()

    def set_first_name(self, first_name):
        self.driver.find_element_by_xpath(self.first_name_id).clear()
        self.driver.find_element_by_xpath(self.first_name_id).send_keys(first_name)

    def set_last_name(self, last_name):
        self.driver.find_element_by_xpath(self.last_name_id).clear()
        self.driver.find_element_by_xpath(self.last_name_id).send_keys(last_name)

    def set_email_address(self, email_address):
        self.driver.find_element_by_xpath(self.email_address_id).clear()
        self.driver.find_element_by_xpath(self.email_address_id).send_keys(email_address)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.password_id).clear()
        self.driver.find_element_by_xpath(self.password_id).send_keys(password)

    def click_register_button(self):
        self.driver.find_element_by_xpath(self.register_button).click()

    def click_register_eye_icon(self):
        self.driver.find_element_by_xpath(self.register_eye_icon).click()

    def click_terms_conditions(self):
        self.driver.find_element_by_xpath(self.terms_conditions).click()

    def click_privacy_policy(self):
        self.driver.find_element_by_xpath(self.privacy_policy).click()

    def click_terms(self):
        self.driver.find_element_by_xpath(self.terms).click()

    def click_yes_join_sephora(self):
        self.driver.find_element_by_xpath(self.yes_join_sephora).click()

    def set_zip_code(self, zip_code):
        self.driver.find_element_by_xpath(self.zip_code).clear()
        self.driver.find_element_by_xpath(self.zip_code).send_keys(zip_code)
