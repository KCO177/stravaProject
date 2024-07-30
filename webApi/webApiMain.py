from webApi.authorization.Authorization import Authorization
from webApi.dataFetcher import DataFetcher

auth_instance = Authorization()
authorizationToken = auth_instance.getAccessToken()

print(DataFetcher.getAllActivities(authorizationToken))
