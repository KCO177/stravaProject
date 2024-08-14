import json

from webApi.dataFetcher.DataFetcher import DataFetcher


class Country:
    def __init__(self, authorizationToken):
        self.athlete = DataFetcher.getAthlete(authorizationToken)
        self.country = self.filterState(self.athlete)

    def filterState(self, athlete):
        country = athlete.get("country")
        return country


# Usage
authorizationToken = "your_authorization_token"
country_instance = Country(authorizationToken)
print(country_instance.country)

