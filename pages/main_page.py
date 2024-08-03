import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class MainPage(Base):

    # Locators
    women_category = '//span[@data-testid="Mw=="]'
    men_category = '//span[@data-testid="NDU="]'
    kids_category = '//span[@data-testid="Nzc="]'
    price_check_box_100_150 = '(//div[@class="sf-radio radio-filter"])[3]'
    ck_category = '//button[@color="CALVIN KLEIN"]'
    sort_by_high_to_low = '(//select[@class="sf-select__dropdown"])[1]'
    size_6_checkbox = '(//label[@class="sf-checkbox__container"])[4]'
    white_color_category = '//button[@data-testid="#ffffff"]'
    apply_filters_button = '//button[@data-testid="apply-filters"]'
    not_on_sale_radio_button = '(//label[@class="sf-radio__container"])[6]'
    product_1 = '//img[@alt="Tommy Hilfiger Distinct Camera Bag"]'
    product_name = '//h1[@class="sf-heading__title h2 text-left"]'
    product_2 = '//img[@alt="Calvin Klein Jeans Suede Trainers"]'
    product_3 = '//img[@alt="Nike Kids Air Force 1 Lv8 3"]'

    # Getters
    def get_women_category(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.women_category)))

    def get_men_category(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.men_category)))

    def get_kids_category(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.kids_category)))

    def get_ck_category(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.ck_category)))

    def get_price_check_box_100_150(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.price_check_box_100_150)))

    def get_sort_by_high_to_low(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sort_by_high_to_low)))

    def get_size_6_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.size_6_checkbox)))

    def get_white_color_category(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.white_color_category)))

    def get_apply_filters_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.apply_filters_button)))

    def get_not_on_sale_radio_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.not_on_sale_radio_button)))

    def get_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1)))

    def get_product_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_name)))

    def get_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_2)))

    def get_product_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_3)))

    # Actions
    def click_women_category(self):  # Click on women category filter
        self.get_women_category().click()
        print('Women category is chosen')

    def click_men_category(self):  # Click on men category filter
        self.get_men_category().click()
        print('Men category is chosen')

    def click_kids_category(self):  # Click on kids category filter
        self.get_kids_category().click()
        print('Kids category is chosen')

    def click_ck_category(self):  # Click on CK category filter
        self.get_ck_category().click()
        print('CK category is chosen')

    def click_sort_by_high_to_low(self):  # Select the last option in the sort by dropdown
        dropdown = self.get_sort_by_high_to_low()
        select = Select(dropdown)
        select.select_by_index(len(select.options) - 1)  # Selecting last option
        print('High to low option in dropdown is chosen')

    def click_size_6_checkbox(self):  # Click on size 6 checkbox
        self.get_size_6_checkbox().click()
        print('Size 6 checkbox is selected')

    def click_white_color_category(self):  # Click on white color category filter
        self.get_white_color_category().click()
        print('White color category is chosen')

    def click_price_check_box_100_150(self):  # Click on 100-150 price checkbox
        self.get_price_check_box_100_150().click()
        print('100-150 price is chosen')

    def click_not_on_sale_radio_button(self):  # Click on not on sale radio button
        self.get_not_on_sale_radio_button().click()
        print('Not on sale filter is chosen')

    def click_apply_filters_button(self):  # Click on apply filters button
        self.get_apply_filters_button().click()
        print('Filters are applied')

    def click_product_1(self):  # Click on product 1
        self.get_product_1().click()
        print('Product 2 is selected')
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.product_name)))

    def click_product_2(self):  # Click on product 2
        self.get_product_2().click()
        print('Product 2 is selected')
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.product_name)))

    def click_product_3(self):  # Click on product 2
        self.get_product_3().click()
        print('Product 3 is selected')
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.product_name)))

    # Methods

    def select_product_1(self):
        self.get_current_url()
        self.click_women_category()  # clicking on women category filter
        self.click_price_check_box_100_150()  # selecting price 100-150 checkbox
        self.scroll_page(900)  # scrolling page down by 200 pixels
        self.click_not_on_sale_radio_button()  # selecting not on sale category
        self.click_apply_filters_button()  # applying filters
        self.scroll_page(200)  # scrolling page down by 200 pixels
        self.click_product_1()  # clicking on product 1 to open its page

    def select_product_2(self):
        self.get_current_url()
        self.click_men_category()  # clicking on men category filter
        self.scroll_page(200)  # scrolling page down by 200 pixels
        self.click_ck_category()  # selecting CK category
        self.click_apply_filters_button()  # applying filters
        self.scroll_page(-200)  # scrolling page up by 200 pixels
        self.click_sort_by_high_to_low()  # choosing option from dropdown
        self.click_product_2()  # clicking on product 2 to open its page

    def select_product_3(self):
        self.get_current_url()
        self.click_kids_category()  # clicking on kids category filter
        self.click_size_6_checkbox()  # selecting size 6 checkbox
        self.scroll_page(400)  # scrolling page down by 200 pixels
        self.click_white_color_category()  # selecting white color category
        self.click_apply_filters_button()  # applying filters
        self.click_product_3()  # clicking on product 3 to open its page
