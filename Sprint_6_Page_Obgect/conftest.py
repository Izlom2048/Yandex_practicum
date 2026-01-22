import pytest
from selenium import webdriver
from Sprint_6_Page_Obgect.pages.main_page import MainPage
from Sprint_6_Page_Obgect.pages.order_page import OrderPage


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def main_page(browser):
    page = MainPage(browser)
    return page

@pytest.fixture(scope="function")
def order_page(browser):
    page = OrderPage(browser)
    return page
