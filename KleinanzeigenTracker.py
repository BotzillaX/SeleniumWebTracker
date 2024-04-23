from searchingForString import main

#url, selectorType(text,href), selector,  chrome_driver_path
#url, selector, chrome_driver_path


chrome_driver_path = "A:\\Desktop\\Scripts\\chromedriver.exe"
url = "https://www.amazon.de/Apple-AirPods-Generation-MagSafe-USB-C/dp/B0CHWZ9TZS/ref=sr_1_3?crid=2SGQMUPKBF890&dib=eyJ2IjoiMSJ9.U2XBkYib7efL-j4R9asbCoryWfD3kbXf7LHWAyyeqqNtTQPTXOHH2NmFD-kTB7MNbBAWDyxGgfmF9RicICZD7XQfZ7NJj2VXV9QIJa8Y5GB92DWbhQ5crQwzOW_0PzzPQhY5fgUUE75FmaZ0PlywWhiEJNV3uaDXyT3BDveWaR18meTGdPRqj86EhHOcUD0Zkco-0P_b6PA33mlPvx-gWBLEFMtbxMDBvkumUE3MTNQ.Lsw2aZF-J3rDFqkgICvrAL3xs54dx9uAyUeHF6kr-ZU&dib_tag=se&keywords=airpods+pro+2&qid=1713902984&sprefix=airpods%2Caps%2C95&sr=8-3&ufe=app_do%3Aamzn1.fos.335e368b-29e8-4542-bb58-939a88195e78"

selector = "#corePriceDisplay_desktop_feature_div > div.a-section.a-spacing-none.aok-align-center.aok-relative > span.a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay > span:nth-child(2) > span.a-price-whole"
selector2 = "#corePriceDisplay_desktop_feature_div > div.a-section.a-spacing-none.aok-align-center.aok-relative > span.a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay > span:nth-child(2) > span.a-price-fraction"


price = 300
while price > 244:
    firstValue = main(url,"text", selector,  chrome_driver_path) #url, selector, chrome_driver_path
    secondValue = main(url,"text", selector2,  chrome_driver_path) #url, selector, chrome_driver_path
    price = int(firstValue)
    firstValue = firstValue + "," + secondValue + "€"
    print(firstValue)
    