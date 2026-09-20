from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


PAGE_URL = (
    "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
)


def test_slow_calculator():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 50)

    try:
        driver.get(PAGE_URL)
        delay = driver.find_element(By.CSS_SELECTOR, "#delay")
        delay.clear()
        delay.send_keys("45")

        for button_text in ("7", "+", "8", "="):
            driver.find_element(
                By.XPATH,
                f"//span[contains(@class, 'btn') and text()='{button_text}']",
            ).click()

        wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15"
            )
        )
        assert driver.find_element(By.CSS_SELECTOR, ".screen").text == "15"
    finally:
        driver.quit()
