from selenium import webdriver

from calculator_page import CalculatorPage


def test_slow_calculator_with_page_object():
    driver = webdriver.Chrome()

    try:
        calculator = CalculatorPage(driver)
        calculator.open()
        calculator.set_delay(45)
        calculator.calculate(("7", "+", "8", "="))

        assert calculator.get_result("15") == "15"
    finally:
        driver.quit()
