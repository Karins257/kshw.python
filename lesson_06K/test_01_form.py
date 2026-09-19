from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


PAGE_URL = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"


def test_form_validation():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get(PAGE_URL)
        values = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro",
        }

        for field_id, value in values.items():
            driver.find_element(By.ID, field_id).send_keys(value)

        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#zip-code.alert-danger")
            )
        )

        zip_class = driver.find_element(By.ID, "zip-code").get_attribute(
            "class"
        )
        assert "alert-danger" in zip_class

        for field_id in values:
            field_class = driver.find_element(
                By.ID, field_id
            ).get_attribute("class")
            assert "alert-success" in field_class
    finally:
        driver.quit()
