import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class ProductsPage(Base):

    # Locators for filters
    product_color_1 = '//button[@data-testid="#000000"]'
    product_color_2 = '//img[@custion-id="Beige"]'
    product_color_3 = '//button[@data-testid="#ffffff"]'
    product_size_1 = '//button[@color="OS"]'
    product_size_2 = '//button[@color="43"]'
    product_size_3 = '//button[@color="6"]'
    add_to_cart_button = '//button[@class="sf-add-to-cart__button rounded-md sf-button"]'
    cart_text = '//div[text()="My Cart"]'
    go_to_checkout_button = '//button[@data-testid="category-sidebar-go-to-checkout"]'

    # Locators for name and price
    product_1_price = '//span[@class="sf-price__regular"]'
    product_1_name = '//h1[@class="sf-heading__title h2 text-left"]'
    cart_product_1_price = '//div[@class="card__price"]'
    cart_product_1_name = '//h3[@class="m-0 font-normal text-xl"]'

    product_2_price = '//span[@class="sf-price__regular"]'
    product_2_name = '//h1[@class="sf-heading__title h2 text-left"]'
    cart_product_2_price = '//div[@class="card__price"]'
    cart_product_2_name = '//h3[@class="m-0 font-normal text-xl"]'

    product_3_price = '//span[@class="sf-price__regular"]'
    product_3_name = '//h1[@class="sf-heading__title h2 text-left"]'
    cart_product_3_price = '//div[@class="card__price"]'
    cart_product_3_name = '//h3[@class="m-0 font-normal text-xl"]'

    # Getters for filters

    def get_product_color_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_color_1)))

    def get_product_color_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_color_2)))

    def get_product_color_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_color_3)))

    def get_product_size_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_size_1)))

    def get_product_size_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_size_2)))

    def get_product_size_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_size_3)))

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    def get_cart_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_text)))

    def get_go_to_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_to_checkout_button)))

    # Getters for name and price
    def get_product_1_price(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.product_1_price)))

    def get_product_1_name(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.product_1_name)))

    def get_cart_product_1_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.cart_product_1_name)))

    def get_cart_product_1_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.cart_product_1_price)))

    def get_product_2_price(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.product_2_price)))

    def get_product_2_name(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.product_2_name)))

    def get_cart_product_2_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.cart_product_2_name)))

    def get_cart_product_2_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.cart_product_2_price)))

    def get_product_3_price(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.product_3_price)))

    def get_product_3_name(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.product_3_name)))

    def get_cart_product_3_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.cart_product_3_name)))

    def get_cart_product_3_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.cart_product_3_price)))

    # Actions for product
    def click_product_color_1(self):  # Click on color
        self.get_product_color_1().click()
        print('Color is chosen')

    def click_product_color_2(self):  # Click on color
        self.get_product_color_2().click()
        print('Color is chosen')

    def click_product_color_3(self):  # Click on color
        self.get_product_color_3().click()
        print('Color is chosen')

    def click_product_size_1(self):  # Click on size
        self.get_product_size_1().click()
        print('Size is chosen')

    def click_product_size_2(self):  # Click on size
        self.get_product_size_2().click()
        print('Size is chosen')

    def click_product_size_3(self):  # Click on size
        self.get_product_size_3().click()
        print('Size is chosen')

    def click_add_to_cart_button(self):  # Click on add to cart button
        self.get_add_to_cart_button().click()
        print('Add to cart button is clicked')

    def click_go_to_checkout_button(self):  # Click checkout button
        self.get_go_to_checkout_button().click()
        print('Checkout is started')

    # Actions for extracting and comparing price and name

    def extract_product_1_details(self):
        product_price = self.get_product_1_price().text
        product_name = self.get_product_1_name().text
        return product_name, product_price

    def extract_cart_product_1_details(self):
        cart_product_name = self.get_cart_product_1_name().text
        cart_product_price = self.get_cart_product_1_price().text
        return cart_product_name, cart_product_price

    def compare_product_details(self, main_name, main_price, cart_name, cart_price):
        assert main_name == cart_name, f"Product names do not match: {main_name} != {cart_name}"
        assert main_price == cart_price, f"Product prices do not match: {main_price} != {cart_price}"
        print("Product name and price match successfully!")

    def extract_product_2_details(self):
        product_price = self.get_product_2_price().text
        product_name = self.get_product_2_name().text
        return product_name, product_price

    def extract_cart_product_2_details(self):
        cart_product_name = self.get_cart_product_2_name().text
        cart_product_price = self.get_cart_product_2_price().text
        return cart_product_name, cart_product_price

    def extract_product_3_details(self):
        product_price = self.get_product_3_price().text
        product_name = self.get_product_3_name().text
        return product_name, product_price

    def extract_cart_product_3_details(self):
        cart_product_name = self.get_cart_product_3_name().text
        cart_product_price = self.get_cart_product_3_price().text
        return cart_product_name, cart_product_price

    # Methods

    def add_to_cart_product_1(self):
        Logger.add_start_step(method='add_to_cart_product_1')
        self.get_current_url()
        self.click_product_color_1()  # choosing color of product
        self.click_product_size_1()  # selecting size of product
        main_name, main_price = self.extract_product_1_details()  # extract details from the main page
        self.click_add_to_cart_button()  # clicking on button to add product to cart
        cart_name, cart_price = self.extract_cart_product_1_details()  # extract details from the cart
        self.compare_product_details(main_name, main_price, cart_name, cart_price)  # compare the details
        self.assert_word(self.get_cart_text(), 'My Cart')  # asserting by word that cart is opened
        self.click_go_to_checkout_button()  # clicking checkout button
        Logger.add_end_step(url=self.driver.current_url, method='add_to_cart_product_1')

    def add_to_cart_product_2(self):
        Logger.add_start_step(method='add_to_cart_product_2')
        self.get_current_url()
        self.click_product_color_2()  # choosing color of product
        self.click_product_size_2()  # selecting size of product
        main_name, main_price = self.extract_product_2_details()  # extract details from the main page
        self.click_add_to_cart_button()  # clicking on button to add product to cart
        cart_name, cart_price = self.extract_cart_product_2_details()  # extract details from the cart
        self.compare_product_details(main_name, main_price, cart_name, cart_price)  # compare the details
        self.assert_word(self.get_cart_text(), 'My Cart')  # asserting by word that cart is opened
        self.click_go_to_checkout_button()  # clicking checkout button
        Logger.add_end_step(url=self.driver.current_url, method='add_to_cart_product_2')

    def add_to_cart_product_3(self):
        Logger.add_start_step(method='add_to_cart_product_3')
        self.get_current_url()
        self.click_product_color_3()  # choosing color of product
        self.click_product_size_3()  # selecting size of product
        main_name, main_price = self.extract_product_3_details()  # extract details from the main page
        self.click_add_to_cart_button()  # clicking on button to add product to cart
        cart_name, cart_price = self.extract_cart_product_3_details()  # extract details from the cart
        self.compare_product_details(main_name, main_price, cart_name, cart_price)  # compare the details
        self.assert_word(self.get_cart_text(), 'My Cart')  # asserting by word that cart is opened
        self.click_go_to_checkout_button()  # clicking checkout button
        Logger.add_end_step(url=self.driver.current_url, method='add_to_cart_product_3')
