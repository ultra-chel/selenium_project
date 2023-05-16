def test_title(driver):
    driver.get("https://ya.ru")
    assert "Яндекс" in driver.title
