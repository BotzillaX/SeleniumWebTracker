import telebot
import undetected_chromedriver as uc

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


Zielpreis = 655
upper = 1
new_angebot = []
Artikel = "apple-watch-ultra"


API_KEY = "5269430439:AAFnMWe2j7V0rPKttrY7ioz9_Mt1U6kOv5E"

bot = telebot.TeleBot(token=API_KEY)

def suche(element_css_selector, driver):
            try:
                wait = WebDriverWait(driver, 10)  # Increase the wait time to 30 seconds

                element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, element_css_selector)))

            # Check if the element contains data before printing the result
                if element.text:
                    text = element.text
                    return text
                else:
                    print("Element found, but it contains no data.")
            except Exception as e:
                print("Error: Could not find the element.")
                
                top = 1
                return top
            
def suche2(upper, Artikel):
    chrome_driver_path = "A:\Desktop\Scripts\chromedriver.exe"
    s = Service(executable_path=chrome_driver_path)
    
    chrome_options = Options()
    options = uc.ChromeOptions()
    #chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(service=s, options=chrome_options)
    driver = uc.Chrome(options=options)
    url = "https://www.kleinanzeigen.de/s-anzeige:angebote/preis:500:750/"+Artikel+"/k0"
    driver.get(url)




    element_css_selector2 = "#srchrslt-adtable > li:nth-child("+str(upper)+") > article > div.aditem-main > div.aditem-main--middle > h2 > a"
    element_css_selector = "#srchrslt-adtable > li:nth-child("+str(upper)+") > article > div.aditem-main > div.aditem-main--middle > div.aditem-main--middle--price-shipping > p"
    element_css_selector3 = "#srchrslt-adtable > li:nth-child("+str(upper)+") > article > div.aditem-main > div.aditem-main--middle > p"
    top_or_not = "#srchrslt-adtable > li:nth-child("+str(upper)+") > article > div.aditem-main > div.aditem-main--top > div.aditem-main--top--right"


    wait = WebDriverWait(driver, 10) 






    first   = suche(element_css_selector, driver)
    second   = suche(element_css_selector2, driver)
    third   = suche(element_css_selector3, driver)
    fourth = suche(top_or_not, driver) #
    if fourth == None:
        top = 1
    else:
        top = 0


    
    print(str(fourth)+ "test") #"1" für nein und "None" für ja
    print(str(first) + " " + str(second) + " //// " + str(third))
    return first, second, third, url, driver, upper, top


def erinnerung(anders, upper, Artikel):
    if anders == " ":
        
        count = 0
        ziel = 20
            
        
        
        while True: 
            
            first, second, third, url, driver, upper, top = suche2(upper, Artikel) #
            
            
            if top == 1:
                upper = upper + 1
            else:
                continue
            
            

            if "Tausch" in second or "Tausche" in second or "TAUSCHE" in second or "TAUSCH" in second:
                print("Tauschangebot")
                print("Suche weiter nach besseren Preis")
                new_angebot.append(second)
                driver.quit()
                
                
            elif "suche" in second or "Suche" in second or "SUCHE" in second or "suchen" in second or "Suchen" in second or "SUCHEN" in second:
                print("Suchangebot")
                print("Suche weiter nach besseren Preis")
                new_angebot.append(second)
                driver.quit()
                
            else:

                preis_länge = len(first)
                if "VB" in first:
                    preis_länge = preis_länge - 2
                    
                preis = first[0:preis_länge-2]
                
                if second in new_angebot:
                    print("Angebot schon vorhanden")
                    print("Suche weiter nach besseren Preis")
                    
                        

                elif second not in new_angebot:
                    print("Preis: " + str(preis))
                    print("Link: " + url)
                    bot.send_message(1432432083, "Preis: " + str(preis) + "€")
                    bot.send_message(1432432083, third)
                    bot.send_message(1432432083, "Link: " + url)
                    bot.send_message(1432432083, "Bitte trage alle leeren Felder logisch selbst ein(ich bin ...). Bitte kurz halten (8 Zeilen max). Schreibe mir eine Kaufanfrage zu einem Verkäufer zu folgenden Infos:"+ second + " " + third +" und Preis: " + str(preis) + "€")
                
                    

                else: 
                    print("Preis ist über 600€")
                    print("Preis: " + str(preis))
                    print(str(int(preis)- int(Zielpreis)) + "€" + " teurer als Wunschpreis")
                    print("Suche weiter nach besseren Preis")
                    


            new_angebot.append(second)
            driver.quit()

    
    else:
        print("sdaiufhaosidfhasodifjaospidfjpoaisdfhpoisadf")
        first, second, third, url, driver, upper, top = suche2(upper, Artikel)
        preis_länge = len(first)
        preis_frage = first[0:preis_länge-2]
        bot.send_message(1432432083, "Preis ist aktuell: " + str(preis_frage) + "€")
        bot.send_message(1432432083, str(int(preis_frage)- int(Zielpreis)) + "€" + " unterschied")
        bot.send_message(1432432083, second)
        bot.send_message(1432432083, third)
        bot.send_message(1432432083, "Link: " + url)
        bot.send_message(1432432083, "Bitte trage alle leeren Felder logisch selbst ein(ich bin ...). Bitte kurz halten (8 Zeilen max). Schreibe mir eine Kaufanfrage zu einem Verkäufer zu folgenden Infos:"+ second + " " + third +" und Preis: " + str(preis) + "€")



        



@bot.message_handler(func=lambda message: "ebay" in message.text)
def greet(message):
    print("es geht")

    erinnerung(" ", upper, Artikel)


@bot.message_handler(func=lambda message: "aktuell" in message.text)
def greet(message):
    print("es geht, ja")
    erinnerung("anders", upper, Artikel)
    



bot.polling()



