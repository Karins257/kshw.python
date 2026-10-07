import allure
from selenium import webdriver

from shop_pages import CartPage
from shop_pages import CheckoutPage
from shop_pages import LoginPage
from shop_pages import ProductsPage


@allure.title("Purchase of three products")
@allure.description(
    "Verify the contents of the cart and the final checkout total."
)
@allure.feature("SauceDemo checkout")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_total_with_page_objects() -> None:
    """Check a SauceDemo purchase through Page Object classes."""
    driver = webdriver.Firefox()
    total = ""

    try:
        login_page = LoginPage(driver)
        products_page = ProductsPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        products_page.add_products(
            (
                "add-to-cart-sauce-labs-backpack",
                "add-to-cart-sauce-labs-bolt-t-shirt",
                "add-to-cart-sauce-labs-onesie",
            )
        )
        products_page.open_cart()

        with allure.step("Check the product names in the cart"):
            assert cart_page.get_item_names() == [
                "Sauce Labs Backpack",
                "Sauce Labs Bolt T-Shirt",
                "Sauce Labs Onesie",
            ]

        cart_page.checkout()
        checkout_page.fill_customer_data("Test", "User", "123456")
        total = checkout_page.get_total()
    finally:
        driver.quit()

    with allure.step("Check the final checkout total"):
        assert total == "Total: $58.29"
