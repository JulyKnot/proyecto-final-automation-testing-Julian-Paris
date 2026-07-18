from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout():

    driver = get_driver()

    try:

        login = LoginPage(driver)
        inventory = InventoryPage(driver)
        cart = CartPage(driver)
        checkout = CheckoutPage(driver)

        print("1 - Login")
        login.open()
        login.login("standard_user", "secret_sauce")

        print("2 - Agregar producto")
        product_name = inventory.get_first_product_name()
        inventory.add_first_product_to_cart()

        print("3 - Abrir carrito")
        inventory.open_cart()

        print("4 - Verificar carrito")
        assert cart.is_product_in_cart(product_name)

        print("5 - Click Checkout")
        checkout.click_checkout()

        print("6 - Completar datos")
        checkout.fill_checkout_information(
            "Julian",
            "Paris",
            "1406"
        )

        print("7 - Finish")
        checkout.finish_checkout()

        print("8 - Validar mensaje")
        assert checkout.get_confirmation_message() == "Thank you for your order!"

    finally:
        driver.quit()