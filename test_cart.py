from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.driver_setup import get_driver


def test_cart_functionality():
    driver = get_driver()
    wait = WebDriverWait(driver, 10)

    try:
        #Login
        driver.get("https://www.saucedemo.com/")

        wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        wait.until(EC.url_contains("inventory.html"))

        #Obtener nombre del PRIMER producto
        first_product = wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
        )[0]

        product_name = first_product.find_element(By.CLASS_NAME, "inventory_item_name").text

        #Agregar primer producto
        add_button = first_product.find_element(By.TAG_NAME, "button")
        add_button.click()

        #Verificar contador del carrito
        cart_badge = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )

        assert cart_badge.text == "1"

        #Ir al carrito
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        wait.until(EC.url_contains("cart.html"))

        #Verificar producto en carrito
        cart_items = wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_name"))
        )

        cart_product_names = [item.text for item in cart_items]

        assert product_name in cart_product_names

        print(f"Producto '{product_name}' agregado y verificado en carrito")

    finally:
        driver.quit()