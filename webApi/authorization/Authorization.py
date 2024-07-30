import requests

from Scripts.webApi.domain import Token

class Authorization:

    def getToken(self):
        token = Token.Token
        token_response = requests.post(
            'https://www.strava.com/oauth/token',
            data={
                'client_id': token.client_id,
                'client_secret': token.client_secret,
                'refresh_token': token.refresh_token,
                'grant_type': 'refresh_token'
            }
        )
        token_data = token_response.json()
        access_token = token_data.get('access_token')

        if not access_token:
            print("Failed to retrieve access token.")
            print(token_data)
        else:
            print("Access token retrieved successfully.")


    def getAllActivities(access_token):
        # Step 2: Use access token to get athlete activities
        activities_url = 'https://www.strava.com/api/v3/athlete/activities'
        headers = {'Authorization': f'Bearer {access_token}'}

        activities_response = requests.get(activities_url, headers=headers)

        # Ensure successful API request
        if activities_response.status_code == 200:
            activities = activities_response.json()
            print(activities)
        else:
            print(f"Error: {activities_response.json()}")
