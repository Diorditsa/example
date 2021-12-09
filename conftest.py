import pytest
from selenium import webdriver
from helpers import helper_function
import allure
from core import seleniumContainer

@pytest.fixture()
def driver():
    capabilities = {
        "browserName": "chrome",
        "browserVersion": "95.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }

    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        desired_capabilities=capabilities)

    # driver =  webdriver.Chrome("/Users/dior/Desktop/chromedriver") # path to driver
    yield driver
    log_console = driver.get_log("browser")
    log_console = helper_function.pretty_log_browser(log_console)
    allure.attach(log_console, name="console log")
    driver.quit()

@pytest.fixture(scope="function")
def selenium_facade(driver):
    return seleniumContainer.SeleniumFacade(driver)