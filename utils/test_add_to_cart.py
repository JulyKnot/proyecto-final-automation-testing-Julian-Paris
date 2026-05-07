from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.driver_setup import get_driver


def test_add_product_to_cart():
    driver = get_driver()
    wait = WebDriverWait(driver, 10)

    try:
        #Login
        driver.get("https://www.saucedemo.com/")

        wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        wait.until(EC.url_contains("inventory.html"))

        #Agregar producto
        add_button = wait.until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        add_button.click()

        #Validar carrito
        cart_badge = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )

        assert cart_badge.text == "1"

        print("✅ Producto agregado correctamente")

    finally:
        driver.quit()