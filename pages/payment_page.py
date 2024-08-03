import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from faker import Faker

from utilities.logger import Logger


class PaymentPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.fake = Faker()

    # Locators
    credit_card_radio = '(//span[@class="sf-radio__checkmark"])[1]'
    card_number = '//input[@data-fieldtype="encryptedCardNumber"]'
    expiry_date = '//input[@aria-label="Expiry date"]'
    cvv_field = '//input[@aria-label="Security code"]'
    name_card = '//input[@name="holderName"]'

    # Getters
    def get_credit_card_radio(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.credit_card_radio)))

    def get_card_number(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.card_number)))

    def get_expiry_date(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.expiry_date)))

    def get_cvv_field(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cvv_field)))

    def get_name_card(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.name_card)))

    # Actions
    def click_credit_card_radio(self):  # Click on credit card radio button
        self.get_credit_card_radio().click()
        print('Credit card payment is chosen')

    def input_card_number(self):  # Input card number
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "card_number"))
            )
            card_number = self.fake.credit_card_number()
            self.get_card_number().send_keys(card_number)
            print('Input card number')
        except TimeoutException:
            print(
                'TimeoutException: element not found')

    def input_expiry_date(self):  # Input expiry date
        expiry_date = self.fake.credit_card_expire()
        self.get_expiry_date().send_keys(expiry_date)
        print('Input expiry date')

    def input_cvv_field(self):  # Input CVV
        cvv_field = self.fake.credit_card_security_code()
        self.clear_and_input(self.get_cvv_field(), cvv_field)
        print('Input CVV')

    def input_name_card(self):  # Input cardholder name
        name_card = self.fake.full_name()
        self.clear_and_input(self.get_name_card(), name_card)
        print('Input cardholder name')

    # Methods

    def final_payment(self):
        Logger.add_start_step(method='final_payment')
        self.get_current_url()
        self.click_credit_card_radio()  # choosing payment by credit card
        self.scroll_page(200)  # scrolling page down by 200 pixels
        self.get_screenshot()  # saving screenshot of final page
        # self.input_card_number()  # возможно по той причине, что данный сайт чей-то прод - с помощью этих методов
        # self.input_expiry_date()  # не получается ввести данные в поля для оплаты картой
        # self.input_cvv_field()
        # self.input_name_card()
        Logger.add_end_step(url=self.driver.current_url, method='final_payment')
