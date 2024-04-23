import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_driver(chrome_driver_path):
    s = Service(executable_path=chrome_driver_path, log_path='NUL')
    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--disk-cache-dir=/path/to/cache')  # Enable caching
    driver = uc.Chrome(service=s, options=chrome_options)
    return driver

def suche(element_css_selector, driver, typeElement):
    try:
        wait = WebDriverWait(driver, 10)  # Adjust wait time as needed
        element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, element_css_selector)))
        href = element.get_attribute('href')

        if typeElement == "text":
            if element.text:
                return element.text
            else:
                print("Element found, but it contains no data.")
        elif typeElement == "href":
            if href:
                return href
            else:
                print("Element gefunden, aber es enthält keine href-Adresse.")
        else:
            print("wrong type " + typeElement)
    except Exception as e:
        print(f"Fehler: Das Element konnte nicht gefunden werden. {e}")
        return None

def main(url, type, element_css_selector, chrome_driver_path):
    driver = setup_driver(chrome_driver_path)
    try:
        driver.get(url)
        result = suche(element_css_selector, driver, type)
        return result
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()  # either href or text
