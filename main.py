from searchingForString import main
from openBrowser import openBrowser1
from pixelDetection import lookingForPixel
from time import sleep
from pyautogui import click
import json

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


currentURLfrommSelector = "#srchrslt-adtable > li:nth-child("+str(count)+") > article > div.aditem-main > div.aditem-main--middle > h2 > a"
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



urlHref = main(url,"href", currentURLfrommSelector,  chrome_driver_path)
openBrowser1(urlHref)
clickingOnPixle("textField")
sleep(1)
clickingOnPixle("message") 
sleep(1)
