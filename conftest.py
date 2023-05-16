import pytest
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="firefox", help="Browser to run test"
    )
    parser.addoption(
        "--driver_storage", default=os.path.expanduser("~/Downloads/drivers"), help="path to browser drivers"
    )


@pytest.fixture()
def driver(request):
    browser_name = request.config.getoption("--browser")
    driver_storage = request.config.getoption("--driver_storage")
    options = Options()
    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    _driver = None

    if browser_name == "chrome":
        _driver = webdriver.Chrome(executable_path=f"{driver_storage}/chromedriver.exe")
    elif browser_name == "ff" or browser_name == "firefox":
        print(driver_storage)
        _driver = webdriver.Firefox(executable_path=f"{driver_storage}/geckodriver.exe", options=options)

    yield _driver

    _driver.close()
