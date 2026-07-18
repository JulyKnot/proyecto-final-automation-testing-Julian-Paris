from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_cart_functionality():

    driver = get_driver()

    try:

        login = LoginPage(driver)
        inventory = InventoryPage(driver)
        cart = CartPage(driver)

        login.open()
        login.login("standard_user", "secret_sauce")

        product_name = inventory.get_first_product_name()

        inventory.add_first_product_to_cart()

        assert inventory.get_cart_badge() == "1"

        inventory.open_cart()

        assert cart.is_product_in_cart(product_name)

        print(f"Producto '{product_name}' agregado correctamente al carrito.")

    finally:
        driver.quit()