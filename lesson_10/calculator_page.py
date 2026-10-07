import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    """Page Object for the slow calculator page."""

    URL = (
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    def __init__(self, driver: WebDriver) -> None:
        """Create the page object for the provided browser driver."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    @allure.step("Open the slow calculator page")
    def open(self) -> None:
        """Open the calculator page in the browser."""
        self.driver.get(self.URL)

    @allure.step("Set calculation delay to {seconds} seconds")
    def set_delay(self, seconds: int) -> None:
        """Set the calculation delay in seconds."""
        delay = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay.clear()
        delay.send_keys(str(seconds))

    @allure.step("Click calculator button '{button_text}'")
    def click_button(self, button_text: str) -> None:
        """Click a calculator button by its visible text."""
        locator = (
            By.XPATH,
            f"//span[contains(@class, 'btn') and text()='{button_text}']",
        )
        self.driver.find_element(*locator).click()

    @allure.step("Enter expression {expression}")
    def calculate(self, expression: tuple[str, ...]) -> None:
        """Enter the supplied sequence of calculator buttons."""
        for button_text in expression:
            self.click_button(button_text)

    @allure.step("Wait for calculation result '{expected_result}'")
    def get_result(self, expected_result: str) -> str:
        """Wait for and return the calculator result text."""
        locator = (By.CSS_SELECTOR, ".screen")
        self.wait.until(
            EC.text_to_be_present_in_element(locator, expected_result)
        )
        return self.driver.find_element(*locator).text
