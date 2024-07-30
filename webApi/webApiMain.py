from webApi.authorization.Authorization import Authorization
from webApi.calculator.CO2calculator import CO2_calculator
from webApi.calculator.CalCalculator import CaloryCalculator
from webApi.dataFetcher.DataFetcher import DataFetcher

auth_instance = Authorization()
authorizationToken = auth_instance.getAccessToken() #get acces token from refresh token
activities = DataFetcher.getAllActivities(authorizationToken) #get all activities
rides = DataFetcher.filterRides(activities)
filteredRides = DataFetcher.filterRideData(rides) #get filtered sum data
CO2_calculator.one_km_weigth(filteredRides) #calculate CO2 save
CaloryCalculator.cal_hour(filteredRides) #calculate cal
