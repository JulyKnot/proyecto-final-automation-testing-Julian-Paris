import pytest

from utils.driver_setup import get_driver
from utils.json_reader import load_login_data
from pages.login_page import LoginPage


@pytest.mark.parametrize("user", load_login_data())
def test_login(user):

    driver = get_driver()

    try:

        login = LoginPage(driver)

        login.open()

        login.login(
            user["username"],
            user["password"]
        )

        if user["valid"]:
            assert login.is_login_successful()
        else:
            assert "Epic sadface" in login.get_error_message()

    finally:
        driver.quit()