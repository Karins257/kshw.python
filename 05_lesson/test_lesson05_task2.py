from selenium import webdriver
from selenium.webdriver.common.by import By


FORM_URL = "https://httpbin.qa-territory.online/forms/post"


def test_form_submission():
    driver = webdriver.Chrome()

    try:
        driver.get(FORM_URL)
        driver.find_element(By.NAME, "custname").send_keys("Карина")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        assert driver.current_url != FORM_URL
        assert driver.current_url.endswith("/post")
    finally:
        driver.quit()
