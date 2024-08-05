from webApi.dataFetcher.PriceHandler import PriceHandler
from webApi.domain.Car import Car
from webApi.domain.Distance import Distance
from webApi.domain.Fuel import Fuel

class CO2_calculator:

    def one_km_weigth(filteredRides):
        fuelType = 'E95' #default value TODO take from ar type
        carType = 'small_SUV'
        category = 'CombinedRoad'
        percentage = 90

        distance = Distance()
        price = PriceHandler()
        fuel = Fuel()
        car = Car()

        litr_fuel: int
        price_fuel: float

        litr_fuel, price_fuel = fuel.get_fuel_data(fuelType, price)
        km = distance.get_sum_of_km(filteredRides)
        avg_l = car.get_value_from_range(carType, category, percentage) # 6.5 AVG consumption of your car for 100 km TODO make input


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
