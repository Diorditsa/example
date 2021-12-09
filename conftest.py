import pytest
from selenium import webdriver
from helpers import helper_function
import allure
from core import seleniumContainer

@pytest.fixture()
def driver():
    driver =  webdriver.Chrome("/Users/dior/Desktop/chromedriver") # path to driver
    yield driver
    log_console = driver.get_log("browser")
    log_console = helper_function.pretty_log_browser(log_console)
    allure.attach(log_console, name="console log")
    # driver.quit()

@pytest.fixture(scope="function")
def selenium_facade(driver):
    return seleniumContainer.SeleniumFacade(driver)