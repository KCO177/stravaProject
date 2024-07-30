import requests
class Authorization:
   def getAccessToken(self):
        from webApi.domain.Token import Token
        token_response = requests.post(
            'https://www.strava.com/oauth/token',
            data={
                'client_id': Token.client_id,
                'client_secret': Token.client_secret,
                'refresh_token': Token.refresh_token,
                'grant_type': 'refresh_token'
            }
        )
        token_data = token_response.json()
        access_token = token_data.get('access_token')

        if not access_token:
            print("Failed to retrieve access token.")
        else:
            print("Access token retrieved successfully")
            return access_token

