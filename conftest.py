import pytest
import os

from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="http://192.168.1.88:8081")
    parser.addoption("--drivers", action="store", default=os.path.expanduser("~/Downloads/drivers"))


# @pytest.fixture()
# def driver(request):
#    browser_name = request.config.getoption("--browser")
#    driver_storage = request.config.getoption("--driver_storage")
#    options = Options()
#    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
#    _driver = None
#
#    if browser_name == "chrome":
#        _driver = webdriver.Chrome(executable_path=f"{driver_storage}/chromedriver.exe")
#    elif browser_name == "ff" or browser_name == "firefox":
#        print(driver_storage)
#        _driver = webdriver.Firefox(executable_path=f"{driver_storage}/geckodriver.exe", options=options)
#
#    yield _driver
#
#    _driver.close()


@pytest.fixture
def browser(request):
    # Сбор параметров запуска для pytest
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    drivers = request.config.getoption("--drivers")

    if browser == "chrome":
        # В selenium 4 рекомендуют использование такого подхода
        service = ChromiumService(executable_path=drivers + "/chromedriver")
        driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        service = FFService(executable_path=drivers + "/geckodriver")
        driver = webdriver.Firefox(service=service)
    # elif browser == "opera":
    #    driver = webdriver.Opera(executable_path=drivers + "/operadriver")
    # else:
    #    driver = webdriver.Safari()

    driver.maximize_window()

    request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url

    return driver
