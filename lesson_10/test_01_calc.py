import allure
from selenium import webdriver

from calculator_page import CalculatorPage


@allure.title("Calculation with a configured delay")
@allure.description("Verify that 7 + 8 is calculated as 15.")
@allure.feature("Slow calculator")
@allure.severity(allure.severity_level.CRITICAL)
def test_slow_calculator_with_page_object() -> None:
    """Check a delayed calculation through the Calculator Page Object."""
    driver = webdriver.Chrome()

    try:
        calculator = CalculatorPage(driver)
        calculator.open()
        calculator.set_delay(45)
        calculator.calculate(("7", "+", "8", "="))

        with allure.step("Check that the result equals 15"):
            assert calculator.get_result("15") == "15"
    finally:
        driver.quit()
