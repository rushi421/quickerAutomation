
import pytest
from selenium import webdriver

@pytest.fixture
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()
        print("Launching chrome browser......")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser......")
    else:
        driver = webdriver.Chrome()
        driver.maximize_window()
    return driver

def pytest_addoption(parser):  # this will get the value from CLI
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): # This will return the browser value into setup method
   return request.config.getoption("--browser")
