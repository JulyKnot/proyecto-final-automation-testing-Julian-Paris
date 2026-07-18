from utils.driver_setup import get_driver
from utils.json_reader import load_login_data
from pages.login_page import LoginPage


def test_invalid_login():

    driver = get_driver()

    try:

        users = load_login_data()

        # Buscar el primer usuario inválido
        invalid_user = next(
            user for user in users
            if not user["valid"]
        )

        login = LoginPage(driver)

        login.open()

        login.login(
            invalid_user["username"],
            invalid_user["password"]
        )

        assert "Epic sadface" in login.get_error_message()

        print("Login inválido validado correctamente.")

    finally:
        driver.quit()