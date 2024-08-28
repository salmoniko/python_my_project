import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.payment_page import PaymentPage
from pages.products_page import ProductsPage


@allure.description('Test buy product 2')
def test_buy_product_2(set_group, set_up):
    options = Options()
    service = Service('C:\\chromedriver\\chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)
    login = LoginPage(driver)
    login.authorization()
    cart = CartPage(driver)
    cart.clean_cart()
    main_page = MainPage(driver)
    main_page.select_product_2()
    products = ProductsPage(driver)
    products.add_to_cart_product_2()
    checkout = CheckoutPage(driver)
    checkout.fill_shipping_info()
    payment = PaymentPage(driver)
    payment.final_payment()
