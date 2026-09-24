from selenium import webdriver

from shop_pages import CartPage
from shop_pages import CheckoutPage
from shop_pages import LoginPage
from shop_pages import ProductsPage


def test_shop_total_with_page_objects():
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

        assert cart_page.get_item_names() == [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie",
        ]

        cart_page.checkout()
        checkout_page.fill_customer_data(
            "Karina", "Suleimanova", "123456"
        )
        total = checkout_page.get_total()
    finally:
        driver.quit()

    assert total == "Total: $58.29"
