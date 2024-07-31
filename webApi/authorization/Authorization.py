from urllib.parse import urlparse, parse_qs
import requests
import webbrowser
from webApi.domain.Token import Token


class Authorization:

    def authorizeUser(self):
        client_id = Token.client_id #get client Id
        redirect_uri = 'http://localhost/exchange_token'
        scope = 'activity:read_all'
        auth_url = f"https://www.strava.com/oauth/authorize?client_id={client_id}&response_type=code&redirect_uri={redirect_uri}&scope={scope}"
        webbrowser.open(auth_url)


    def get_refresh_token(client_id, code):
        token_response = requests.post(
        'https://www.strava.com/oauth/token',
        data = {
            'client_id': client_id,
            'client_secret': Token.client_secret,
            'code': Token.code,
            'grant_type': 'authorization_code'
            }
        )
        token_data = token_response.json()
        refresh_token = token_data.get('refresh_token')
        if not refresh_token:
            print("Failed to retrieve access token.")
        else:
            print("Access token retrieved successfully")
            return refresh_token

    def getAccessToken(self,client_id):
        token_instance = Token()
        token_response = requests.post(
            'https://www.strava.com/oauth/token',
            data={
                'client_id': client_id,
                'client_secret': token_instance.fetch_data(client_id,"refresh_token","client_secret"),
                'refresh_token': token_instance.fetch_data(client_id,"refresh_token","refresh_token"),
                'grant_type': 'refresh_token'
            }
        )
        token_data = token_response.json()
        access_token = token_data.get('access_token')
        expiration = token_data.get('expires_at')
        if not access_token:
            print("Failed to retrieve access token.")
        else:
            print("Access token retrieved successfully")
            return access_token, expiration
    '''
    how to call
    token, expiration_timestamp = get_access_token_info()
    print(f"Access Token: {token}")
    print(f"Expiration Timestamp: {expiration_timestamp}")
    '''



