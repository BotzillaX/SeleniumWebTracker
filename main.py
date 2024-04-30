from searchingForString import main
from openBrowser import openBrowser1
from pixelDetection import lookingForPixel
from time import sleep
from pyautogui import click
import json
from keyboard import press_and_release, write
from AIOllama import ollamaGPT


with open("C:\\Users\\kevin\\Dropbox\\Kundenwunsch\\Wagner An- und Verkauf\\Kundenwunsch.json", "r") as json_File:
    loadedJSON = json.load(json_File)


def clickingOnPixle(object): #clicking on nachrichten and text
    val = lookingForPixel(object)[1]
    while val  < 0.90:
        val = lookingForPixel(object)[1]
        sleep(0.1)
    x, y = lookingForPixel(object)[0]
    click(x, y)            





while True:
    Wunschpreis = loadedJSON["Wunschpreis"]
    chrome_driver_path = loadedJSON["chrome_driver_path"]
    url = loadedJSON["url"]
    count = 1

    
    price = Wunschpreis+ Wunschpreis
    while price > Wunschpreis:
        if main(url,"text", "#srchrslt-adtable > li:nth-child("+str(count)+") > article > div.aditem-main > div.aditem-main--top > div.aditem-main--top--right",  chrome_driver_path) == False:
            price+=Wunschpreis #disable leaving loop if item is top prio
            count+=1
            print("skipped")
        else:
            priceFirstSlot = main(url,"text", "#srchrslt-adtable > li:nth-child("+str(count)+") > article > div.aditem-main > div.aditem-main--middle > div.aditem-main--middle--price-shipping > p",  chrome_driver_path) #url, selector, chrome_driver_path
            price = "" 
            for char in priceFirstSlot:
                if char in ["0","1","2","3","4","5","6","7","8","9",","]:
                    price+=char
            price = int(price)
            if price <= Wunschpreis:
                count=1 #reset count to go back to first item becasue maybe there are no top prios anymore
            else:
                pass
            pass
        
        
        
        print(price)


        urlHref = main(url,"href", "#srchrslt-adtable > li:nth-child("+str(count)+") > article > div.aditem-main > div.aditem-main--middle > h2 > a",  chrome_driver_path)
        titel = main(urlHref,"text", "#viewad-title",  chrome_driver_path)
        describ = main(urlHref,"text", "#viewad-description-text",  chrome_driver_path)
        sellerName = main(urlHref,"text", "#viewad-contact > div > ul > li > span > span.text-body-regular-strong.text-force-linebreak.userprofile-vip",  chrome_driver_path)
        print(titel)
        print(describ)
        print(sellerName)
        sleep(0.5)
        openBrowser1(urlHref)
        sleep(0.5)
        clickingOnPixle("message1")
        sleep(0.5)
        clickingOnPixle("textField") 

        

        theMessage = ollamaGPT("act as a buyer who is interested in an item, you only text in german and never in englisch:  TITEL: "+titel+", Beschreibung: "+describ+" und Verkäufer: "+sellerName+", Preis: "+str(price)+".")

        write(theMessage)