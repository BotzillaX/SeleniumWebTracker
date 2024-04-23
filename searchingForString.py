import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def suche(element_css_selector, driver, typeElement):
    try:
        wait = WebDriverWait(driver, 15)  
        element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, element_css_selector)))
        href = element.get_attribute('href')
        


        if typeElement == "text":
            if element.text:
                    text = element.text
                    return text
            else:
                print("Element found, but it contains no data.")
        elif typeElement == "href":
            if href:
                return href
            else:
                print("Element gefunden, aber es enthält keine href-Adresse.")
        else:
             print("wrong type "+ typeElement)
    except Exception as e:
        print(f"Fehler: Das Element konnte nicht gefunden werden. {e}")
        return None

def main(artikel, type):
    artikel.lower().replace(" ", "-")
    chrome_driver_path = "A:\\Desktop\\Scripts\\chromedriver.exe"
    s = Service(executable_path=chrome_driver_path, log_path='NUL')  
    
    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument('--log-level=3')  

    try:
        driver = uc.Chrome(service=s, options=chrome_options)
        
        url = f"https://www.kleinanzeigen.de/s-anzeige:angebote/preis:500:750/{artikel}/k0"
        driver.get(url)

        element_css_selector = "#srchrslt-adtable > li:nth-child(1) > article > div.aditem-main > div.aditem-main--middle > h2 > a"
        result = suche(element_css_selector, driver, type)
        print(result)
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
    finally:
        driver.quit()





if __name__ == "__main__":
    main("apple watch ultra", "href") #either href or text 
