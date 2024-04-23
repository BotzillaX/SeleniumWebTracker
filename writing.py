import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.kleinanzeigen.de/s-anzeige/apple-watch-ultra-2-wie-neu-/2741300895-173-1345"
selector = "#email"
chrome_driver_path = "A:\\Desktop\\Scripts\\chromedriver.exe"

def setup_driver(chrome_driver_path):
    s = Service(executable_path=chrome_driver_path)
    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
    chrome_options.add_argument("--window-size=1920x1080")  # Specify window size
    driver = uc.Chrome(service=s, options=chrome_options)
    return driver

def suche2(url, selector, chrome_driver_path):
    driver = setup_driver(chrome_driver_path)
    try:
        driver.get(url)
        wait = WebDriverWait(driver, 10)  # Adjusted wait time to a reasonable value
        email_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        email_field.send_keys("kevinfritsch7@yahoo.de")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()  # Ensure the driver is quit properly

if __name__ == "__main__":
    suche2(url, selector, chrome_driver_path)
