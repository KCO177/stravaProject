from webApi.authorization.Authorization import Authorization
from webApi.authorization.Token import Token
from webApi.dataFetcher import DataFilter
from webApi.dataFetcher.DataFetcher import DataFetcher


auth_instance = Authorization()
token_instance = Token()
clientId = 106674

authorizationToken = token_instance.fetch_access_token(clientId) #get acces token from refresh token
athlete = DataFetcher.getAthlete(authorizationToken) #get all activities
print(athlete)


print(DataFilter.DataFilter.filterCountry(athlete))