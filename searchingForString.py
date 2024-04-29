import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

# Konfigurieren des Loggings
logging.basicConfig(level=logging.ERROR)

def setup_driver(chrome_driver_path):
    s = Service(executable_path=chrome_driver_path, log_path='NUL')
    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--disk-cache-dir=/path/to/cache')  # Enable caching
    try:
        driver = uc.Chrome(service=s, options=chrome_options)
    except Exception as e:
        logging.error(f"Driver konnte nicht initialisiert werden: {e}")
        return None
    return driver

def suche(element_css_selector, driver, typeElement):
    if driver is None:
        return None
    try:
        wait = WebDriverWait(driver, 10)  # Adjust wait time as needed
        element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,element_css_selector )))
        href = element.get_attribute('href')

        if typeElement == "text":
            return element.text if element.text else False
        elif typeElement == "href":
            return href if href else False
        else:
            return "wrong type " + typeElement
    except Exception as e:
        logging.error(f"Fehler: Das Element konnte nicht gefunden werden. {e}")
        return None

def main(url, type, element_css_selector, chrome_driver_path):
    driver = setup_driver(chrome_driver_path)
    if driver is None:
        return "Driver konnte nicht initialisiert werden."
    try:
        driver.get(url)
        return suche(element_css_selector, driver, type)
    except Exception as e:
        logging.error(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    main()  # either href or text