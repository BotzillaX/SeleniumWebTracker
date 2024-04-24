from searchingForString import main
from openBrowser import openBrowser1

Wunschpreis = 4600
chrome_driver_path = "A:\\Desktop\\Scripts\\chromedriver.exe"
url = "https://www.kleinanzeigen.de/s-preis:1200:/ninja-125/k0"
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
            
    
    
    