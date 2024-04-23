from searchingForString import main

#url, selectorType(text,href), selector,  chrome_driver_path
#url, selector, chrome_driver_path


chrome_driver_path = "A:\\Desktop\\Scripts\\chromedriver.exe"
url = "https://www.amazon.de/dp/B0BW9DFPWN?psc=1&ref=ppx_yo2ov_dt_b_product_details"

selector = "#corePriceDisplay_desktop_feature_div > div.a-section.a-spacing-none.aok-align-center.aok-relative > span.a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay > span:nth-child(2) > span.a-price-whole"
selector2 = "#corePriceDisplay_desktop_feature_div > div.a-section.a-spacing-none.aok-align-center.aok-relative > span.a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay > span:nth-child(2) > span.a-price-fraction"




firstValue = main(url,"text", selector,  chrome_driver_path) #url, selector, chrome_driver_path
secondValue = main(url,"text", selector2,  chrome_driver_path) #url, selector, chrome_driver_path

firstValue = firstValue + "," + secondValue + "€"
print(firstValue)