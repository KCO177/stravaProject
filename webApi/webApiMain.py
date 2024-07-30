from webApi.authorization.Authorization import Authorization
from webApi.calculator.Calculator import CO2_calculator
from webApi.dataFetcher.DataFetcher import DataFetcher

auth_instance = Authorization()
authorizationToken = auth_instance.getAccessToken() #get acces token from refresh token
activities = DataFetcher.getAllActivities(authorizationToken) #get all activities
rides = DataFetcher.filterRideData(activities) #get filtered sum data
CO2_calculator.one_km_weigth(rides[0]) #calculate CO2 save
CO2_calculator.cal_hour(rides[1]) #calculate cal
