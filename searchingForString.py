import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import subprocess

def suche(element_css_selector, driver):
    try:
        wait = WebDriverWait(driver, 10)  # Wartezeit auf 10 Sekunden gesetzt
        element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, element_css_selector)))
        href = element.get_attribute('href')
        if href:
            return href
        else:
            print("Element gefunden, aber es enthält keine href-Adresse.")
    except Exception as e:
        print(f"Fehler: Das Element konnte nicht gefunden werden. {e}")
        return None

def main():
    chrome_driver_path = "A:\\Desktop\\Scripts\\chromedriver.exe"
    s = Service(executable_path=chrome_driver_path, log_path='NUL')  # Unterdrückt die WebDriver-Logs

    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument('--log-level=3')  # Setzt das Logging-Level auf Fehlermeldungen

    driver = None
    try:
        driver = uc.Chrome(service=s, options=chrome_options)
        artikel = "apple-watch-ultra"
        url = f"https://www.kleinanzeigen.de/s-anzeige:angebote/preis:500:750/{artikel}/k0"
        driver.get(url)

        element_css_selector = "#srchrslt-adtable > li:nth-child(1) > article > div.aditem-main > div.aditem-main--middle > h2 > a"
        result = suche(element_css_selector, driver)
        print(result)
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
    finally:
        if driver:
            driver.quit()
            # Forcefully kill any remaining Chrome processes
            subprocess.call(['taskkill', '/F', '/IM', 'chromedriver.exe'])
            subprocess.call(['taskkill', '/F', '/IM', 'chrome.exe'])

if __name__ == "__main__":
    main()
