import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class CartPage(Base):

    # Locators
    close_cart_button = '//div[@class="cursor-pointer"]'
    cart_button = '//button[@aria-label="Toggle cart sidebar"]'
    clean_cart_button = '//img[@alt="trash"]'
    empty_cart_text = '//h2[@class="sf-heading__title h2"]'

    # Getters
    def get_close_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.close_cart_button)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    def get_clean_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.clean_cart_button)))

    def get_empty_cart_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.empty_cart_text)))

    # Actions
    def click_close_cart_button(self):  # Click close cart button
        self.get_close_cart_button().click()
        print('Close cart button is clicked')

    def click_cart_button(self):  # Click cart button
        self.get_cart_button().click()
        print('Cart button is clicked')

    def click_clean_cart_button(self):  # Click trash button to clean cart
        try:
            self.get_clean_cart_button().click()
            print('Cart is cleaned')
        except TimeoutException:
            print('Cart is empty')

    # Methods

    def clean_cart(self):
        self.get_current_url()
        self.click_cart_button()  # opening cart
        self.click_clean_cart_button()  # deleting products from cart
        self.assert_word(self.get_empty_cart_text(), 'Your cart is empty')  # checking if cart is empty
        self.click_close_cart_button()  # clicking on close cart button
