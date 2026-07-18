from utils.driver_setup import get_driver
from pages.login_page import LoginPage


def test_login():

    driver = get_driver()

    try:

        login = LoginPage(driver)

        login.open()
        login.login("standard_user", "secret_sauce")

        assert login.is_login_successful()

        print("Login realizado correctamente.")

    finally:
        driver.quit()