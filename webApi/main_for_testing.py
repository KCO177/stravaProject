from webApi.dataFetcher.PriceHandler import PriceHandler

price = PriceHandler()
print(price.getValidPrices())

#result = (price.getPrices())[0]
#date = result[1]
#print (date)

#price.setPrices('04.08.2024', '38.050', '36.530')