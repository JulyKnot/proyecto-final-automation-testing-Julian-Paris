import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver_setup import get_driver


def test_login_saucedemo():
    driver = get_driver()
    wait = WebDriverWait(driver, 10)

    try:
        #Navegación de página
        driver.get("https://www.saucedemo.com/")

        #Ingreso de usuario
        username_input = wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        username_input.send_keys("standard_user")

        #Ingreso de contraseña
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys("secret_sauce")

        #Click en botó de login
        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()

        #Validar redirección a inventory
        wait.until(EC.url_contains("inventory.html"))

        assert "inventory.html" in driver.current_url

        #Validar que aparece "Products"
        products_title = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "title"))
        )

        assert products_title.text == "Products"

        #Validar Swag Labs (header)
        header = driver.find_element(By.CLASS_NAME, "app_logo")
        assert header.text == "Swag Labs"

        print("✅ Login exitoso validado correctamente")

    finally:
        driver.quit()