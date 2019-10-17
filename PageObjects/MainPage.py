from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class MainPage:
    # Locators of all elements
#    browser = webdriver.Chrome("C:/Users/Tudor/PycharmProjects/Sephora/Drivers/chromedriver.exe")
#    browser = webdriver.Firefox()
    reorder_link = "//*[@id='Header']/div[2]/div/div/div[2]/a[1]"
    track_order_link = "//*[@id='Header']/div[2]/div/div/div[2]/a[2]"
    verify_reorder_link = "//h1[text()='Purchases']"
    verify_track_order = "//*[text()='ORDER STATUS & HISTORY']"
    close_x_icon = "//*[@id='modalDialog']/button"
    find_store_link = "//a[@data-at='find_in_store']"
    verify_find_store = "//a[text()='Find a Sephora']"
    # Example of finding elements by partial xpath
    just_arrived_items = "/html/body/div[2]/div[5]/main/div/div[2]/div/div/div[2]//div[contains(@id, 'tabItem')]"
    editors_picks_items = "/html/body/div[2]/div[5]/main/div/div[4]/div/div/div[2]//div[contains(@id, 'tabItem')]"
    palettes_value_items = "/html/body/div[2]/div[5]/main/div/div[5]/div/div/div[2]//div[contains(@id, 'tabItem')]"
    recommended_items = "/html/body/div[2]/div[5]/main/div/div[6]/div/div/div[2]//div[contains(@id, 'tabItem')]"
    spot_shop_items = "//div[@class='css-1e01tr8 ']"
    something_beautiful = "//*[@id='10120322']"
    verify_smth_beautiful = "//*[@id='10320311']"
    about_sephora_link = "//a[@title='About Sephora']"
    verify_about_sephora = "//strong[text()='About Us']"
    careers_link = "//a[@title='Careers']"
    verify_careers_link = "//h2[@class='h3 fontcolorae422a2fccc3554c fontalign-center']"
    social_impact_link = "//a[@title='Sephora Stands Social Impact']"
    verify_social_impact = "//h2[text()='We belong to something beautiful']"
    affiliates_link = "//a[@title='Affiliates']"
    verify_affiliates = "//h1[@id='sephora-affiliates']"
    supply_chain_link = "//a[@title='Supply Chain Transparency']"
    verify_supply_chain = "//h1[@id='supply-chain-transparency']"
    sitemap_link = "//a[@title='Sitemap']"
    verify_sitemap = "//h1[@class='css-1sihb80 ']"
    sephora_global_link = "//a[@title='Sephora Global Sites']"
    verify_sephora_global = "//strong[text()='Sephora International']"
    sephoria_link = "//a[@title='Sephoria']"
    facebook_icon = "//*[@data-comp='IconFacebook Icon Box']"
    verify_facebook = "//a[@href='https://www.facebook.com/sephora/']"
    twitter_icon = "//*[@data-comp='IconTwitter Icon Box']"
    verify_twitter = "//title[text()='Sephora (@Sephora) | Twitter']"
    instagram_icon = "//*[@data-comp='IconInstagram Icon Box']"
    verify_instagram = "//title[text()='Sephora (@sephora) • Instagram photos and videos']"
    youtube_icon = "//*[@data-comp='IconYoutube Icon Box']"
    verify_youtube = "//title[text()='Sephora - YouTube']"
    terms_use_link = "//a[text()='Terms of Use']"
    verify_terms_use = "//*[text()='TERMS OF USE']"
    privacy_policy_link = "//a[text()='Privacy Policy']"
    verify_privacy_policy = "//*[text()='PRIVACY POLICY']"
    mouseover_shop = "//*[@id='topnav_menu0_trigger']/div/div[2]"
    makeup_link = "//a[@href='/shop/makeup-cosmetics']"
    skincare_link = "//a[@href='/shop/skincare']"
    main_page_link = "//img[@alt='Sephora']"
    hair_link = "//a[@href='/shop/hair-products']"
    tools_brushes_link = "//a[@href='/shop/makeup-tools']"
    fragrance_link = "//a[@href='/shop/fragrance']"
    bath_body_link = "//a[@href='/shop/bath-body']"
    gifts_link = "//a[@href='/shop/gifts']"
    sale_link = "//a[@href='/sale']"
    site_search = "//input[@id='site_search_input']"
    search_result = "//*[@class='css-ix8km1']"
    dropdown_sort_by = "//div[@id='cat_sort_menu_trigger']"
    price_high_low = "//button[@class='css-1hkefft ' and text()='Price High to Low']"
    price_low_high = "//button[@class='css-1hkefft ' and text()='Price Low to High']"
    verify_high_low = "//button[@aria-current='true' and text()='Price High to Low']"
    verify_low_high = "//button[@aria-current='true' and text()='Price Low to High']"
    sliders = "//div[@role='slider']"
    prices_50_150 = "//span[@data-at='sku_item_price_list']"
    reset_filters = "(//button[text()='Reset all filters'])[2]"
    search_skincare_link = "//button[@class='css-h6ss0r ' and text()='Skincare']"
    verify_skincare_1 = "/html/body/div[2]/div[5]/div/div/div/div[2]/div/div/nav/button[2]"
    verify_skincare_2 = "//div[@class='css-12egk0t']"
    brand_name = "//button[text()='Brand Name']"
    verify_brand_name = "//button[@aria-current='true' and text()='Brand Name']"
    mouseover_gifts = "//div[@class='css-1ljtfew ' and text()='Gifts']"
    ten_and_under = "//a[@data-at='nth_level_category' and text()='$10 and Under']"
    prices_under_ten = "//span[@data-at='sku_item_price_list']"
    mouseover_brands = "//div[@class='css-1ljtfew ' and text()='Brands']"
    brands_a_z = "//a[@title='Brands A-Z']"
    brand_dior = "//a[@href='/brand/dior']"
    verify_dior = "//span[@data-at='sku_item_brand' and text()='Dior']"
    view_all_gifts = "//a[@href='/shop/all-gifts']"
    clinique_checkbox = "/html/body/div[2]/div[5]/div/div/div/div[2]/div[1]/div/div/div[2]/fieldset/div[30]/label/div[1]"
    verify_clinique = "//span[@data-at='sku_item_brand' and text()='CLINIQUE']"
    mouseover_new = "//div[@class='css-1ljtfew ' and text()='New']"
    verify_new = "//div[@class='css-8o71lk' and text()='NEW']"
    number_of_products = "//span[@data-at='number_of_products']"
    click_page_2 = "//button[@class='css-1f9ivf5 ']"

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.sephora.com/"

    def click_brand_name_link(self):
        self.driver.find_element_by_xpath(self.brand_name).click()

    def click_skincare_link(self):
        self.driver.find_element_by_xpath(self.search_skincare_link).click()

    def click_reset_filters(self):
        self.driver.find_element_by_xpath(self.reset_filters).click()

    def set_sliders(self):
        # Selecting all sliders
        sliders = self.driver.find_elements_by_xpath(self.sliders)
        left_slider = sliders[0]
        right_slider = sliders[1]
        move = ActionChains(self.driver)
        # Moving the left slider
        move.click_and_hold(left_slider).move_by_offset(50, 0).release().perform()
        # Moving the right slider
        move.click_and_hold(right_slider).move_by_offset(-10, 0).release().perform()

    def click_price_low_high(self):
        self.driver.find_element_by_xpath(self.price_low_high).click()

    def click_price_high_low(self):
        self.driver.find_element_by_xpath(self.price_high_low).click()

    def click_dropdown_sort_by(self):
        self.driver.find_element_by_xpath(self.dropdown_sort_by).click()

    def scroll_down_page_lights(self):
        self.driver.execute_script("window.scrollBy(0, 750)", "")
        time.sleep(0.2)

    def scroll_bottom_page(self):
        self.driver.execute_script("window.scrollBy(0, 5000)", "")
        time.sleep(0.2)

    def scroll_down_page(self):
        self.driver.execute_script("window.scrollBy(0, 500)", "")
        time.sleep(0.2)
        self.driver.execute_script("window.scrollBy(0, 500)", "")
        time.sleep(0.2)
        self.driver.execute_script("window.scrollBy(0, 500)", "")
        time.sleep(0.2)
        self.driver.execute_script("window.scrollBy(0, 500)", "")
        time.sleep(0.2)
        self.driver.execute_script("window.scrollBy(0, 500)", "")
        time.sleep(0.2)
        self.driver.execute_script("window.scrollBy(0, 500)", "")
        time.sleep(0.2)

    def set_site_search(self, search_item):
        self.driver.find_element_by_xpath(self.site_search).clear()
        self.driver.find_element_by_xpath(self.site_search).send_keys(search_item)
        self.driver.find_element_by_xpath(self.site_search).send_keys(Keys.ENTER)

    def click_main_page(self):
        self.driver.find_element_by_xpath(self.main_page_link).click()

    def browser_back_button(self):
        self.driver.execute_script('window.history.go(-1)')

    def click_something_beautiful(self):
        self.driver.find_element_by_xpath(self.something_beautiful).click()

    def click_find_store_link(self):
        self.driver.find_element_by_xpath(self.find_store_link).click()

    def click_reorder_link(self):
        self.driver.find_element_by_xpath(self.reorder_link).click()

    def click_track_order_link(self):
        self.driver.find_element_by_xpath(self.track_order_link).click()

    def click_close_x_icon(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, self.close_x_icon)))
        element.click()

