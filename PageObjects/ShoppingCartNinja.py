from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

__author__ = "Tudor C"


class ShoppingCartNinja:
    # Locators of all elements
#    browser = webdriver.Chrome("C:/Users/Tudor/PycharmProjects/Sephora/Drivers/chromedriver.exe")
#    browser = webdriver.Firefox()
    my_account_link = "//*[@class='hidden-xs hidden-sm hidden-md' and text()='My Account']"
    login_link = "//a[text()='Login']"
    email_id = "//*[@id='input-email']"
    password_id = "//*[@id='input-password']"
    login_button = "//input[@class='btn btn-primary']"
    logout_link = "//*[@class='list-group-item' and text()='Logout']"
    top_logout_link = "//*[@id='top-links']/ul/li[2]/ul/li[5]/a"
    main_page = "//*[text()='The Ninja Store']"
    add_item_1 = "//*[@id='content']/div[2]/div[1]/div/div[3]/button[1]/span"
    add_item_2 = "//*[@id='content']/div[2]/div[2]/div/div[3]/button[1]/span"
    shopping_cart = "//*[text()='Shopping Cart']"
    elem_1 = "//*[@id='content']/div[2]/div[1]/div/div[2]/h4/a"
    elem_2 = "//*[@id='content']/form/div/table/tbody/tr/td[2]/a"
    wish_list_button = "//*[@id='content']/div[2]/div[1]/div/div[3]/button[2]/i"
    wish_list_link = "//*[@id='wishlist-total']/span"
    wishlist_elem = "//*[@id='content']/div[1]/table/tbody/tr/td[2]/a"
    remove_button = "//*[@data-original-title='Remove']"
    addtocart_button = "//*[@data-original-title='Add to Cart']"
    checkout_button = "//a[text()='Checkout']"
    returning_customer = "//*[text()='Returning Customer']"
    black_button_id = "//*[@id='cart-total']"
    black_button_remove = "//*[@class='fa fa-times']"
    black_button_empty_text = "//*[text()='Your shopping cart is empty!']"
    price_item_1 = "//*[@id='content']/div[2]/div[1]/div/div[2]/p[2]/span"
    price_item_2 = "//*[@id='content']/div[2]/div[2]/div/div[2]/p[2]/span"
    total_price = "//*[@id='content']/div[2]/div/table/tbody/tr[2]/td[2]"
    quantity_field = "//*[@id='content']/form/div/table/tbody/tr/td[4]/div/input"
    update_button = "//*[@class='fa fa-refresh']"
    verify_product = "//*[@id='content']/form/div/table/tbody/tr/td[2]/a"
    coupon_code = "//*[@id='accordion']/div[1]/div[1]/h4/a"
    gift_certificate = "//*[@id='accordion']/div[2]/div[1]/h4/a"
    checkout_login_button = "//*[@id='button-login']"

    def __init__(self, driver):
        self.driver = driver
        self.url = "http://tutorialsninja.com/demo/index.php?route=common/home"

    def click_my_account_link(self):
        self.driver.find_element_by_xpath(self.my_account_link).click()

    def click_login_link(self):
        self.driver.find_element_by_xpath(self.login_link).click()

    def set_email(self, email):
        self.driver.find_element_by_xpath(self.email_id).clear()
        self.driver.find_element_by_xpath(self.email_id).send_keys(email)

    def set_quantity(self, quantity):
        self.driver.find_element_by_xpath(self.quantity_field).clear()
        self.driver.find_element_by_xpath(self.quantity_field).send_keys(quantity)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.password_id).clear()
        self.driver.find_element_by_xpath(self.password_id).send_keys(password)

    def click_login_button(self):
        self.driver.find_element_by_xpath(self.login_button).click()

    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout_link).click()

    def click_top_logout_link(self):
        self.driver.find_element_by_xpath(self.top_logout_link).click()

    def click_main_page(self):
        self.driver.find_element_by_xpath(self.main_page).click()

    def click_add_item_1(self):
        self.driver.find_element_by_xpath(self.add_item_1).click()

    def click_add_item_2(self):
        self.driver.find_element_by_xpath(self.add_item_2).click()

    def click_shopping_cart(self):
        self.driver.find_element_by_xpath(self.shopping_cart).click()

    def click_wish_list_button(self):
        self.driver.find_element_by_xpath(self.wish_list_button).click()

    def click_wish_list_link(self):
        self.driver.find_element_by_xpath(self.wish_list_link).click()

    def click_remove_button(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.remove_button))).click()

    def click_addtocart_button(self):
        self.driver.find_element_by_xpath(self.addtocart_button).click()

    def click_checkout_button(self):
        self.driver.find_element_by_xpath(self.checkout_button).click()

    def click_black_button_id(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.black_button_id))).click()

    def click_black_button_remove(self):
        self.driver.find_element_by_xpath(self.black_button_remove).click()

    def click_update_button(self):
        self.driver.find_element_by_xpath(self.update_button).click()

    def click_checkout_login_button(self):
        self.driver.find_element_by_xpath(self.checkout_login_button).click()











