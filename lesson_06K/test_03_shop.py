from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


PAGE_URL = "https://www.saucedemo.com/"


def test_shop_total():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)
    total = ""

    try:
        driver.get(PAGE_URL)
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        product_ids = (
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bolt-t-shirt",
            "add-to-cart-sauce-labs-onesie",
        )
        for product_id in product_ids:
            wait.until(EC.element_to_be_clickable((By.ID, product_id))).click()

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
        driver.find_element(By.ID, "first-name").send_keys("Karina")
        driver.find_element(By.ID, "last-name").send_keys("Suleimanova")
        driver.find_element(By.ID, "postal-code").send_keys("123456")
        driver.find_element(By.ID, "continue").click()

        total_locator = (By.CLASS_NAME, "summary_total_label")
        total = wait.until(
            EC.visibility_of_element_located(total_locator)
        ).text
    finally:
        driver.quit()

    assert total == "Total: $58.29"
