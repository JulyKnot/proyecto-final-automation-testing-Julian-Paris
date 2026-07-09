from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_cart_items(self):
        return self.wait.until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "inventory_item_name")
            )
        )

    def get_product_names(self):
        return [item.text for item in self.get_cart_items()]

    def is_product_in_cart(self, product_name):
        return product_name in self.get_product_names()

    def get_items_count(self):
        return len(self.get_cart_items())