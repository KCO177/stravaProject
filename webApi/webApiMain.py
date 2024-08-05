from webApi.authorization.Authorization import Authorization
from webApi.authorization.Token import Token
from webApi.calculator.CO2calculator import CO2_calculator
from webApi.calculator.CalCalculator import CaloryCalculator
from webApi.dataFetcher.DataFetcher import DataFetcher

auth_instance = Authorization()
token_instance = Token()
clientId = 106674

authorizationToken = token_instance.fetch_access_token(clientId) #get acces token from refresh token
activities = DataFetcher.getAllActivities(authorizationToken) #get all activities
rides = DataFetcher.filterRides(activities)

filteredRides = DataFetcher.filterRideData(rides) #get filtered sum data
CO2_calculator.one_km_weigth(filteredRides) #calculate CO2 save
CaloryCalculator.cal_hour(filteredRides) #calculate cal
