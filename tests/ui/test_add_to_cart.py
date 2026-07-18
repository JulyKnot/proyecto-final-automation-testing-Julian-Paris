from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_add_product_to_cart():

    driver = get_driver()

    try:

        login = LoginPage(driver)
        inventory = InventoryPage(driver)

        login.open()
        login.login("standard_user", "secret_sauce")

        inventory.add_first_product_to_cart()

        assert inventory.get_cart_badge() == "1"

        print("Producto agregado correctamente al carrito.")

    finally:
        driver.quit()