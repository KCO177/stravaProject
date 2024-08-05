from webApi.dataFetcher.PriceHandler import PriceHandler


class CO2_calculator:

    def one_km_weigth(filteredRides, fuelType):
        km = int(filteredRides['Distance'].sum()) / 1000
        litr_fuel: int
        price_fuel: float
        price = PriceHandler()
        if fuelType == "benzin":
            litr_fuel = 2390  #weigth [g] CO2 per 1 litr
            price_fuel = float(price.getValidPrices()[2])
        elif fuelType == "nafta":
            litr_fuel = 2640  #weigth [g] CO2 per 1 litr
            price_fuel = float(price.getValidPrices()[3])
        else:
            print("not supported fuel")  #TODO move to the domain

        avg_l = 6.5  #AVG consumption of your car for 100 km TODO make input

        one_km = litr_fuel * avg_l / 100
        total_km = round((km / 100) * avg_l, 2)
        print('total consuption', total_km)
        total = round(one_km * km / 1000, 2)
        price = round(price_fuel * total_km, 2)
        print('for one km: ', one_km, 'g of CO2')
        print('for all rides you save: ', total, 'kg of CO2')
        print('you save', total_km, 'l in price:', price, 'Kc')
        #print('today you save', total, 'kg of CO2')
        #print('you should save', week,'kg in week')
