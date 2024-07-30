import pandas as pd

from webApi.dataFetcher.DataFetcher import DataFetcher
from webApi.domain.Bike import Bike


class CaloryCalculator:

    def cal_hour(filteredRides):

        duration = int(filteredRides['Moving Time'].sum()) / 3600

        calories = 0
        for _, row in filteredRides.iterrows():
            value_ride = CaloryCalculator.setRideDifficulty(row)
            calories += value_ride

        calories_per_minute_cycling = calories / 60  # Calories burned per minute for moderate cycling on a mountain bike
        total_cal = round(duration * calories_per_minute_cycling, 2)
        print('You burn a total of', total_cal, 'calories')
        return total_cal

    def setRideDifficulty(filteredRides):
        distance = filteredRides['Distance']
        elevation = filteredRides['Elevation Gain']
        sport_type = filteredRides['Ride Type']
        ride_type_map = {
            'MountainBikeRide': 'mountainBike',
            'Ride': 'roadBike',
            'GravelBikeRide': 'gravelBike',
        }
        ride_type = ride_type_map.get(sport_type)
        difficultyCoef = elevation / distance
        difficulty = ""
        if 20 >= difficultyCoef: difficulty = "Easy"
        if 20 < difficultyCoef < 40: difficulty = "Moderate"
        if 40 >= difficultyCoef: difficulty = 'Intense'

        return Bike.get_bike_value(ride_type + difficulty)

