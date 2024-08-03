import time

from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class LoginPage(Base):
    url = 'https://www.hudsonstore.com/'

    # Locators
    account_button = '//button[@data-testid="accountIcon"]'  # locator for account button
    email_field = '//input[@id="email"]'  # locator for email field
    password_field = '//input[@id="password"]'  # locator for password field
    sign_in_button = '//button[@type="submit"]'  # locator for submit login button
    log_out_button = '//button[@data-testid="Log out"]'  # locator for logout button
    error_message_1 = '//div[@class="notifications"]'  # locator for error message with wrong data
    error_message_2 = '(//div[@class="sf-input__error-message"])[1]'  # locator for error message with empty fields

    # Getters
    def get_account_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.account_button)))

    def get_email_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.email_field)))

    def get_password_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.password_field)))

    def get_sign_in_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.sign_in_button)))

    def get_log_out_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.log_out_button)))

    def get_error_message_1(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.error_message_1)))

    def get_error_message_2(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.error_message_2)))

    # Actions
    def click_account_button(self):  # Click on account button to input credentials
        self.get_account_button().click()
        print('Account button is clicked')
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.email_field)))
        except TimeoutException:
            print("Email field is not visible after clicking account button")

    def input_email(self, email):
        self.get_email_field().send_keys(email)  # Input data in email field
        print('Input email')

    def input_password(self, password):  # Input data in password field
        self.get_password_field().send_keys(password)
        print('Input password')

    def click_sign_in_button(self):  # Click on sign in button to log in
        self.get_sign_in_button().click()
        print('Clicked submit sign in button')  # here might be some problems don't forget
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.log_out_button)))
        except TimeoutException:
            print("Log out button not visible after clicking sign in button")

    def click_log_out_button(self):  # Check if log out button is displayed after successful log in
        self.get_log_out_button().click()
        print("Log out button clicked")
        time.sleep(2)

    def assertion_login(self):  # Check if log out button is displayed after successful log in
        try:
            assert self.get_log_out_button().is_displayed()
            print("Log in SUCCESSFUL")
        except TimeoutException:
            print("User is logged out")

    def assertion_error_message_1(self):  # Check error message appears if input incorrect credentials
        assert self.get_error_message_1().is_displayed()
        print("Log in UNSUCCESSFUL - wrong data")

    def assertion_error_message_2(self):  # Check error message appears if try to log in with empty fields
        assert self.get_error_message_2().is_displayed()
        print("Log in UNSUCCESSFUL - empty fields")

    # Methods

    def authorization(self):
        Logger.add_start_step(method='authorization')
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()  # checking current URL
        self.click_account_button()  # clicking on account button to start log in
        self.input_email('123bug456report@gmail.com')  # inputting email
        self.input_password('Lightpass123')  # inputting password
        self.click_sign_in_button()  # clicking sign in button to confirm log in
        self.click_account_button()  # clicking on my profile button to see log out button is displayed
        self.assertion_login()  # verifying log out button is displayed
        Logger.add_end_step(url=self.driver.get_current_url, method='authorization')

    def auth_invalid_password(self):
        Logger.add_start_step(method='auth_invalid_password')
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()  # checking current URL
        self.click_account_button()  # clicking on account button to start log in
        self.input_email('123bug456report@gmail.com')  # inputting email
        self.input_password('WrongPassword123')  # inputting wrong password
        self.click_sign_in_button()  # clicking sign in button to confirm log in
        self.assertion_error_message_1()  # asserting that log in is unsuccessful
        Logger.add_end_step(url=self.driver.get_current_url, method='auth_invalid_password')

    def auth_invalid_login(self):
        Logger.add_start_step(method='auth_invalid_login')
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()  # checking current URL
        self.click_account_button()  # clicking on account button to start log in
        self.input_email('wrongemail@gmail.com')  # inputting wrong email
        self.input_password('Lightpass123')  # inputting password
        self.click_sign_in_button()  # clicking sign in button to confirm log in
        self.assertion_error_message_1()  # asserting that log in is unsuccessful
        Logger.add_end_step(url=self.driver.get_current_url, method='auth_invalid_login')

    def auth_empty_fields(self):
        Logger.add_start_step(method='auth_empty_fields')
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()  # checking current URL
        self.click_account_button()  # clicking on account button to start log in
        self.input_email('')  # inputting empty email
        self.input_password('')  # inputting empty password
        self.assertion_error_message_2()  # asserting that log in is unsuccessful
        Logger.add_end_step(url=self.driver.get_current_url, method='auth_empty_fields')

    def log_out(self):
        Logger.add_start_step(method='log_out')
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()  # checking current URL
        self.click_account_button()  # clicking on account button to start log in
        self.input_email('123bug456report@gmail.com')  # inputting email
        self.input_password('Lightpass123')  # inputting password
        self.click_sign_in_button()  # clicking sign in button to confirm log in
        self.click_account_button()  # clicking on my profile button to see log out button is displayed
        self.click_log_out_button()  # user is logged out
        self.click_account_button()  # clicking account button to check log out button is not displayed
        self.assertion_login()  # asserting log out button is not displayed
        Logger.add_end_step(url=self.driver.get_current_url, method='log_out')
