from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        ).click()

    def fill_checkout_information(self, first_name, last_name, postal_code):

        first = self.wait.until(
            EC.visibility_of_element_located((By.ID, "first-name"))
        )
        first.clear()
        first.send_keys(first_name)

        last = self.driver.find_element(By.ID, "last-name")
        last.clear()
        last.send_keys(last_name)

        postal = self.driver.find_element(By.ID, "postal-code")
        postal.clear()
        postal.send_keys(postal_code)

        # Mostrar qué quedó escrito
        print("First:", first.get_attribute("value"))
        print("Last:", last.get_attribute("value"))
        print("Postal:", postal.get_attribute("value"))

        self.driver.find_element(By.ID, "continue").click()

        print("URL:", self.driver.current_url)

    def finish_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "finish"))
        ).click()

    def get_confirmation_message(self):
        return self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
        ).text