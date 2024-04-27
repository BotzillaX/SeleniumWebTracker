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


def clickingOnPixle(object):
    val = lookingForPixel(object)[1]
    while val  < 0.90:
        val = lookingForPixel(object)[1]
        sleep(0.1)
    x, y = lookingForPixel(object)[0]
    click(x, y)            

    


Wunschpreis = loadedJSON["Wunschpreis"]
chrome_driver_path = loadedJSON["chrome_driver_path"]
url = loadedJSON["url"]
count = 1

#url, selectorType(text, href), selector,  chrome_driver_path
#url, selector, chrome_driver_path


currentSelector = "#srchrslt-adtable > li:nth-child("+str(count)+") > article > div.aditem-main > div.aditem-main--middle > h2 > a"
currentPrice =  "#srchrslt-adtable > li:nth-child("+str(count)+") > article > div.aditem-main > div.aditem-main--middle > div.aditem-main--middle--price-shipping > p"


price = Wunschpreis+ 1000
while price > Wunschpreis:
    priceFirstSlot = main(url,"text", currentPrice,  chrome_driver_path) #url, selector, chrome_driver_path
    price = "" 
    for char in priceFirstSlot:
        if char in ["0","1","2","3","4","5","6","7","8","9"]:
            price+=char
    price = int(price)
    print(price)



urlHref = main(url,"href", currentSelector,  chrome_driver_path)
openBrowser1(urlHref)
sleep(1)
clickingOnPixle("message1")
sleep(1)
clickingOnPixle("textField") 

titel = main(urlHref,"text", "#viewad-title",  chrome_driver_path)
describ = main(urlHref,"text", "#viewad-description-text",  chrome_driver_path)
sellerName = main(urlHref,"text", "#viewad-contact > div > ul > li > span > span.text-body-regular-strong.text-force-linebreak.userprofile-vip",  chrome_driver_path)

theMessage = ollamaGPT("act as a buyer who is interested in an item, you only text in german and never in englisch:  TITEL: "+titel+", Beschreibung: "+describ+" und Verkäufer: "+sellerName+", Preis: "+str(price)+".")

write(theMessage)