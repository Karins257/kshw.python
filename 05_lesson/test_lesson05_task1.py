from selenium import webdriver
from selenium.webdriver.common.by import By


BASE_URL = "https://httpbin.qa-territory.online/"


def test_navigation():
    driver = webdriver.Chrome()

    try:
        driver.get(BASE_URL)
        driver.find_element(By.LINK_TEXT, "HTML Form").click()

        assert driver.current_url == f"{BASE_URL}forms/post"

        driver.back()

        assert driver.current_url == BASE_URL
    finally:
        driver.quit()
