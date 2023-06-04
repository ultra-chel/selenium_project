from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WaitTime:
    FAST = 1
    MEDIUM = 2
    SLOW = 3


class MainPage:
    LOGO = (By.CSS_SELECTOR, "#logo")
    MENU_BAR = (By.CSS_SELECTOR, "ul.nav.navbar-nav > li.nav-item")
    SEARCH_BAR = (By.ID, "search")
    FEATURED_PRODUCT = (By.CLASS_NAME, "product-thumb")
    FOOTER = (By.XPATH, "//footer//ul")


def test_main_page_check_logo(browser):
    browser.get(browser.url + "/")
    browser.find_element(*MainPage.LOGO)
    WebDriverWait(browser, WaitTime.FAST).until(
        EC.visibility_of_element_located(MainPage.LOGO),
        message=f"Logo of the page {MainPage.LOGO} was not loaded in {WaitTime.FAST} seconds"
    )


def test_main_check_search_bar(browser):
    menu_items = browser.find_element(*MainPage.SEARCH_BAR)


def test_main_page_menu_bar(browser):
    menu_items = browser.find_elements(*MainPage.MENU_BAR)
    assert len(menu_items) == 8, "Неверное количество элементов меню"


def test_main_page_fetured_items(browser):
    fetured_items = browser.find_elements(*MainPage.FEATURED_PRODUCT)
    assert len(fetured_items) == 4, "Неверное количество продуктов в блоке featured"


def test_main_page_footer_blocks(browser):
    footer_blocks = browser.find_elements(*MainPage.FOOTER)
    assert len(footer_blocks) == 4, "Неверное количество списков ссылок в футере"
