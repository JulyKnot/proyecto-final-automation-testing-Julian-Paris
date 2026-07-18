from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_inventory_page():

    driver = get_driver()

    try:

        login = LoginPage(driver)
        inventory = InventoryPage(driver)

        login.open()
        login.login("standard_user", "secret_sauce")

        assert inventory.get_title() == "Products"
        assert len(inventory.get_products()) > 0

        print(f"Primer producto: {inventory.get_first_product_name()}")
        print(f"Precio: {inventory.get_first_product_price()}")

        assert inventory.is_menu_displayed()
        assert inventory.is_filter_displayed()

        print("Inventario validado correctamente.")

    finally:
        driver.quit()