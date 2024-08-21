from webApi.authorization.Authorization import Authorization
from webApi.authorization.Token import Token
from webApi.dataFetcher import DataFilter
from webApi.dataFetcher.DataFetcher import DataFetcher

class Athlete():

    def getAthleteCountry(clientId):

        token_instance = Token()
        authorizationToken = token_instance.fetch_access_token(clientId)  # get acces token from refresh token
        athlete = DataFetcher.getAthlete(authorizationToken)  # get all activities

        return (DataFilter.DataFilter.filterCountry(athlete))


