import time

import allure
from selenium.common import TimeoutException, StaleElementReferenceException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from faker import Faker


class CheckoutPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.fake = Faker()

    # Locators
    shipping_button = '//button[@type="submit"]'
    shipping_address_title = '(//h3[@class="sf-heading__title h3"])[1]'
    first_name = '//input[@id="firstName"]'
    last_name = '//input[@id="lastName"]'
    street_name = '//input[@id="streetName"]'
    house_number = '//input[@name="apartment"]'
    city_name = '//input[@aria-labelledby="vs2__combobox"]'
    zip_code = '//input[@id="zipCode"]'
    phone_number = '//input[@id="telephone"]'
    shipping_method = '//div[@class="form__action"]'
    standard_delivery_radio = '//label[@class="sf-radio__container"]'
    continue_billing_button = '//button[@class="form__action-button sf-button"]'
    continue_payment_button = '//div[@class="form__action"]'

    # Getters

    def get_shipping_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.shipping_button)))

    def get_shipping_address_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.shipping_address_title)))

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_street_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.street_name)))

    def get_house_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.house_number)))

    def get_city_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city_name)))

    def get_zip_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.zip_code)))

    def get_phone_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_number)))

    def get_shipping_method(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.shipping_method)))

    def get_standard_delivery_radio(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.standard_delivery_radio)))

    def get_continue_billing_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.continue_billing_button)))

    def get_continue_payment_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.continue_payment_button)))

    # Actions
    def click_shipping_button(self):  # Click go to shipping button
        try:
            self.get_shipping_button().click()
            print('Shipping info page is opened')
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, self.shipping_address_title)))
            except TimeoutException:
                print("Name field is not displayed")
        except StaleElementReferenceException:
            print("Encountered StaleElementReferenceException, retrying...")
            # Retry the click action
            self.get_shipping_button().click()
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, self.shipping_address_title)))
            except TimeoutException:
                print("Name field is not displayed")
        time.sleep(1)  # in this case time sleep was used as even with exceptions error happens

    def input_first_name(self):  # Input first name
        first_name = self.fake.first_name()
        self.clear_and_input(self.get_first_name(), first_name)
        print('Input first name')

    def input_last_name(self):  # Input last name
        last_name = self.fake.last_name()
        self.clear_and_input(self.get_last_name(), last_name)
        print('Input last name')

    def input_street_name(self):  # Input street name
        street_name = self.fake.street_name()
        self.clear_and_input(self.get_street_name(), street_name)
        print('Input street name')

    def input_house_number(self):  # Input house name
        house_number = self.fake.building_number()
        self.clear_and_input(self.get_house_number(), house_number)
        print('Input house name')

    def input_city_name(self):  # Input city name and click 'Enter'
        self.get_city_name().send_keys('Marfa')
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ENTER).perform()
        print('City is chosen')

    def input_zip_code(self):  # Input last name
        zip_code = self.fake.zipcode()
        self.clear_and_input(self.get_zip_code(), zip_code)
        print('Input zip code')

    def input_phone_number(self):  # Input last name
        self.get_phone_number().clear()
        self.clear_and_input(self.get_phone_number(), '8855458569')
        print('Input phone number')

    def click_shipping_method(self):  # Click go to shipping button
        self.get_shipping_method().click()
        print('Shipping method is clicked')

    def click_standard_delivery_radio(self):  # Click go to shipping button
        self.get_standard_delivery_radio().click()
        print('Standard shipping is chosen')

    def click_continue_billing_button(self):  # Click go to continue billing button button
        self.get_continue_billing_button().click()
        print('Continue billing button is clicked')
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.continue_payment_button)))
        except TimeoutException:
            print("Payment button is not visible")

    def click_continue_payment_button(self):  # Click go to continue payment button button
        self.get_continue_payment_button().click()
        print('Continue payment button is clicked')

    # Methods

    def fill_shipping_info(self):
        with allure.step('Fill shipping info'):
            self.get_current_url()
            self.click_shipping_button()  # clicking on shipping button to move to next screen
            self.input_first_name()  # inputting random first name
            self.input_last_name()  # inputting random last name
            self.input_street_name()  # # inputting random street name
            self.input_house_number()  # inputting random house number
            self.input_city_name()  # inputting city name
            self.input_zip_code()  # inputting random zip code
            self.input_phone_number()  # inputting phone number
            self.click_shipping_method()  # clicking on shipping method button
            self.scroll_page(200)  # scrolling page down by 200 pixels
            self.click_standard_delivery_radio()  # clicking on standard delivery radio
            self.click_continue_billing_button()  # clicking on continue billing button
            self.click_continue_payment_button()  # clicking on continue payment button
