import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from pages.login_page import LoginPage


@pytest.mark.order(1)
def test_correct_login(set_group, set_up):
    options = Options()
    service = Service('C:\\chromedriver\\chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)
    login = LoginPage(driver)
    login.authorization()


@pytest.mark.order(3)
def test_invalid_email_login(set_group, set_up):
    options = Options()
    service = Service('C:\\chromedriver\\chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)
    login = LoginPage(driver)
    login.auth_invalid_login()


@pytest.mark.order(2)
def test_invalid_password_login(set_group, set_up):
    options = Options()
    service = Service('C:\\chromedriver\\chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)
    login = LoginPage(driver)
    login.auth_invalid_password()


@pytest.mark.order(4)
def test_empty_fields_login(set_group, set_up):
    options = Options()
    service = Service('C:\\chromedriver\\chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)
    login = LoginPage(driver)
    login.auth_empty_fields()


@pytest.mark.order(5)
def test_log_out(set_group, set_up):
    options = Options()
    service = Service('C:\\chromedriver\\chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)
    login = LoginPage(driver)
    login.log_out()
