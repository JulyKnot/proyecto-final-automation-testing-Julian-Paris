from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.driver_setup import get_driver


def test_inventory_page():
    driver = get_driver()
    wait = WebDriverWait(driver, 10)

    try:
        # Log in
        driver.get("https://www.saucedemo.com/")

        wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Esperar que cargue inventario
        wait.until(EC.url_contains("inventory.html"))

        # 1. Validar título de la página
        title = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "title"))
        )
        assert title.text == "Products"

        # 2. Validar que haya productos visibles
        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(products) > 0

        # 3. Obtener nombre y precio del primer producto
        first_product_name = products[0].find_element(By.CLASS_NAME, "inventory_item_name").text
        first_product_price = products[0].find_element(By.CLASS_NAME, "inventory_item_price").text

        print(f" Producto: {first_product_name}")
        print(f" Precio: {first_product_price}")

        # 4. Validar elementos importantes de la UI

        # Menú 
        menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
        assert menu_button.is_displayed()

        # Filtro de productos
        filter_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
        assert filter_dropdown.is_displayed()

        # Carrito
        cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        assert cart_icon.is_displayed()

        print("Navegación e inventario validados correctamente")

    finally:
        driver.quit()