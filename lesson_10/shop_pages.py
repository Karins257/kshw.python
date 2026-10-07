import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    """Page Object for the SauceDemo login page."""

    URL = "https://www.saucedemo.com/"

    def __init__(self, driver: WebDriver) -> None:
        """Create the page object for the provided browser driver."""
        self.driver = driver

    @allure.step("Open the SauceDemo login page")
    def open(self) -> None:
        """Open the login page in the browser."""
        self.driver.get(self.URL)

    @allure.step("Log in as '{username}'")
    def login(self, username: str, password: str) -> None:
        """Log in with the supplied username and password."""
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()


class ProductsPage:
    """Page Object for the SauceDemo products page."""

    def __init__(self, driver: WebDriver) -> None:
        """Create the page object for the provided browser driver."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Add products to the cart: {product_ids}")
    def add_products(self, product_ids: tuple[str, ...]) -> None:
        """Add products to the cart by their element identifiers."""
        for product_id in product_ids:
            locator = (By.ID, product_id)
            self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Open the shopping cart")
    def open_cart(self) -> None:
        """Open the shopping cart page."""
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()


class CartPage:
    """Page Object for the SauceDemo shopping cart page."""

    def __init__(self, driver: WebDriver) -> None:
        """Create the page object for the provided browser driver."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Read product names from the cart")
    def get_item_names(self) -> list[str]:
        """Return the visible names of all products in the cart."""
        locator = (By.CLASS_NAME, "inventory_item_name")
        items = self.wait.until(
            EC.visibility_of_all_elements_located(locator)
        )
        return [item.text for item in items]

    @allure.step("Proceed to checkout")
    def checkout(self) -> None:
        """Open the checkout information page."""
        locator = (By.ID, "checkout")
        self.wait.until(EC.element_to_be_clickable(locator)).click()


class CheckoutPage:
    """Page Object for the SauceDemo checkout page."""

    def __init__(self, driver: WebDriver) -> None:
        """Create the page object for the provided browser driver."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Fill customer data for {first_name} {last_name}")
    def fill_customer_data(
        self,
        first_name: str,
        last_name: str,
        postal_code: str,
    ) -> None:
        """Fill in customer data and continue to the overview page."""
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    @allure.step("Read the checkout total")
    def get_total(self) -> str:
        """Return the visible checkout total text."""
        locator = (By.CLASS_NAME, "summary_total_label")
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).text
