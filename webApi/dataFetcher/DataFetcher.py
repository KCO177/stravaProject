import json
import requests
import pandas as pd


class DataFetcher():
    def getAthlete(access_token):
        athlete_url = 'https://www.strava.com/api/v3/athlete'
        headers = {'Authorization': f'Bearer {access_token}'}

        athlete_response = requests.get(athlete_url, headers=headers)

        # Ensure successful API request
        if athlete_response.status_code == 200:
            athlete = athlete_response.json()
            return (athlete)
        else:
            print(f"Error: {athlete_response.json()}")

    def getAllActivities(access_token):
        # Step 2: Use access token to get athlete activities
        activities_url = 'https://www.strava.com/api/v3/athlete/activities'
        headers = {'Authorization': f'Bearer {access_token}'}

        activities_response = requests.get(activities_url, headers=headers)

        # Ensure successful API request
        if activities_response.status_code == 200:
            activities = activities_response.json()
            return (activities)
        else:
            print(f"Error: {activities_response.json()}")


    def filterRideData(rides):
        filtered_ride = pd.DataFrame(rides)
        filtered_ride['Activity Date'] = pd.to_datetime(filtered_ride['start_date_local'])
        filtered_ride['Activity Type'] = filtered_ride['type']
        filtered_ride['Ride Type'] = filtered_ride['sport_type']
        filtered_ride['Moving Time'] = filtered_ride['moving_time']
        filtered_ride['Distance'] = filtered_ride['distance']
        filtered_ride['Elevation Gain'] = filtered_ride['total_elevation_gain']

        #TODO this block only for dev check remove this
        strava_df_filtered = filtered_ride[['Activity Date', 'Activity Type','Ride Type', 'Moving Time', 'Distance', 'Elevation Gain']]
        print('strava_df_filtered')
        print(strava_df_filtered)

        return strava_df_filtered


