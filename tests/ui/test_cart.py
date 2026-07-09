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

        # Login
        login.open()
        login.login("standard_user", "secret_sauce")

        # Obtener nombre del primer producto
        product_name = inventory.get_first_product_name()

        # Agregar al carrito
        inventory.add_first_product_to_cart()

        # Verificar contador
        assert inventory.get_cart_badge() == "1"

        # Abrir carrito
        inventory.open_cart()

        # Verificar producto
        assert cart.is_product_in_cart(product_name)

        print(f"Producto '{product_name}' agregado y verificado correctamente.")

    finally:
        driver.quit()