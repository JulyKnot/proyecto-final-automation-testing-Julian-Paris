from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_title(self):
        return self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "title"))
        ).text

    def get_products(self):
        return self.driver.find_elements(By.CLASS_NAME, "inventory_item")

    def get_first_product_name(self):
        products = self.get_products()
        return products[0].find_element(By.CLASS_NAME, "inventory_item_name").text

    def get_first_product_price(self):
        products = self.get_products()
        return products[0].find_element(By.CLASS_NAME, "inventory_item_price").text

    def add_first_product_to_cart(self):
        products = self.get_products()
        products[0].find_element(By.TAG_NAME, "button").click()

    def get_cart_badge(self):
        return self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        ).text

    def open_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    def is_menu_displayed(self):
        return self.driver.find_element(
            By.ID,
            "react-burger-menu-btn"
        ).is_displayed()

    def is_filter_displayed(self):
        return self.driver.find_element(
            By.CLASS_NAME,
            "product_sort_container"
        ).is_displayed()