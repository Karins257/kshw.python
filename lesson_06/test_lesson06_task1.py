from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


PAGE_URL = "https://the-internet.herokuapp.com/dynamic_loading/2"
SCREENSHOT_PATH = Path(__file__).with_name("dynamic_loading.png")


def test_dynamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get(PAGE_URL)
        wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button"))
        ).click()

        message = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#finish h4")
            )
        )
        driver.save_screenshot(str(SCREENSHOT_PATH))

        assert message.text == "Hello World!"
    finally:
        driver.quit()
