from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_driver():

    chrome_options = Options()

    chrome_options.add_argument("--start-maximized")

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }

    chrome_options.add_experimental_option("prefs", prefs)

    chrome_options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(options=chrome_options)

    return driver