from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    URL = (
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self):
        self.driver.get(self.URL)

    def set_delay(self, seconds):
        delay = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay.clear()
        delay.send_keys(str(seconds))

    def click_button(self, button_text):
        locator = (
            By.XPATH,
            f"//span[contains(@class, 'btn') and text()='{button_text}']",
        )
        self.driver.find_element(*locator).click()

    def calculate(self, expression):
        for button_text in expression:
            self.click_button(button_text)

    def get_result(self, expected_result):
        locator = (By.CSS_SELECTOR, ".screen")
        self.wait.until(
            EC.text_to_be_present_in_element(locator, expected_result)
        )
        return self.driver.find_element(*locator).text
