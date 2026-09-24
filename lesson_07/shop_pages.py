from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_products(self, product_ids):
        for product_id in product_ids:
            locator = (By.ID, product_id)
            self.wait.until(EC.element_to_be_clickable(locator)).click()

    def open_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_item_names(self):
        locator = (By.CLASS_NAME, "inventory_item_name")
        items = self.wait.until(
            EC.visibility_of_all_elements_located(locator)
        )
        return [item.text for item in items]

    def checkout(self):
        locator = (By.ID, "checkout")
        self.wait.until(EC.element_to_be_clickable(locator)).click()


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_customer_data(self, first_name, last_name, postal_code):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    def get_total(self):
        locator = (By.CLASS_NAME, "summary_total_label")
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).text
