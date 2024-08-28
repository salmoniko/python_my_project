import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from pages.login_page import LoginPage


@allure.description('Test correct login')
# @pytest.mark.order(1)
def test_correct_login(set_group, set_up):
    options = Options()
    service = Service('C:\\chromedriver\\chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)
    login = LoginPage(driver)
    login.authorization()


@allure.description('Test invalid email login')
# @pytest.mark.order(3)
def test_invalid_email_login(set_group, set_up):
    options = Options()
    service = Service('C:\\chromedriver\\chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)
    login = LoginPage(driver)
    login.auth_invalid_login()


@allure.description('Test invalid password login')
# @pytest.mark.order(2)
def test_invalid_password_login(set_group, set_up):
    options = Options()
    service = Service('C:\\chromedriver\\chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)
    login = LoginPage(driver)
    login.auth_invalid_password()


@allure.description('Test empty fields login')
# @pytest.mark.order(4)
def test_empty_fields_login(set_group, set_up):
    options = Options()
    service = Service('C:\\chromedriver\\chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)
    login = LoginPage(driver)
    login.auth_empty_fields()


@allure.description('Test log out')
# @pytest.mark.order(5)
def test_log_out(set_group, set_up):
    options = Options()
    service = Service('C:\\chromedriver\\chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)
    login = LoginPage(driver)
    login.log_out()
