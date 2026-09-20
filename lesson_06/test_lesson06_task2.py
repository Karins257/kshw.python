import json
import os

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


BASE_URL = "https://gitflic.ru/"
USER_1_URL = f"{BASE_URL}user/nextsm1le_hw6"
USER_2_URL = f"{BASE_URL}user/salamander6789_hw6"


def get_cookies(variable_name):
    """Read previously obtained cookies without publishing them in Git."""
    value = os.environ.get(variable_name)
    assert value, f"Set the {variable_name} environment variable"
    return json.loads(value)


def add_cookies(driver, cookies):
    for cookie in cookies:
        driver.add_cookie(cookie)


def test_different_gitflic_users():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get(BASE_URL)
        add_cookies(driver, get_cookies("GITFLIC_USER_1_COOKIES"))
        driver.refresh()
        driver.get(USER_1_URL)
        wait.until(EC.url_to_be(USER_1_URL))
        user_1_url = driver.current_url

        driver.delete_all_cookies()
        add_cookies(driver, get_cookies("GITFLIC_USER_2_COOKIES"))
        driver.refresh()
        driver.get(USER_2_URL)
        wait.until(EC.url_to_be(USER_2_URL))
        user_2_url = driver.current_url

        assert user_1_url != user_2_url
    finally:
        driver.quit()
