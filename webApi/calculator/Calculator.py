class CO2_calculator:

    def one_km_weigth(km):
        # weigth [g] CO2 for 1 litr
        #litr_nafta = 2640
        litr_benzin = 2390
        cena_ben = 36.7
        avg_l = 6.5 #AVG consumption of your car for 100 km

        one_km = litr_benzin*avg_l/100
        total_km = round((km/100) * avg_l, 2)
        print('total consuption', total_km)
        total = round(one_km * km/1000, 2)
        price = round(cena_ben * total_km, 2)
        print('for one km: ',one_km, 'g of CO2')
        print('for all rides you save: ', total, 'kg of CO2')
        print('you save', total_km, 'l in price:', price, 'Kc')
        #print('today you save', total, 'kg of CO2')
        #print('you should save', week,'kg in week')

    def cal_hour(duration):
        #from mountain bike moderate cycling
        minute_cycling = 791/60
        total_cal = round(duration*minute_cycling, 2)
        print('you burn total', total_cal,'cal')
        #print('you should burn additional', total_cal*5,'cal in one week' )
