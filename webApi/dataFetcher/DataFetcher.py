import json
import requests
import pandas as pd

class DataFetcher:
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

    def filterRideData(activities):
        rides = [activity for activity in activities if activity['type'] == 'Ride']
        filtered_ride = pd.DataFrame(rides)
        filtered_ride['Activity Date'] = pd.to_datetime(filtered_ride['start_date_local'])
        filtered_ride['Activity Type'] = filtered_ride['type']
        filtered_ride['Elapsed Time'] = filtered_ride['elapsed_time']
        filtered_ride['Distance'] = filtered_ride['distance'] / 1000  # Convert from meters to kilometers

        #TODO this block only for dev check remove this
        strava_df_filtered = filtered_ride[['Activity Date', 'Activity Type', 'Elapsed Time', 'Distance']]
        print(strava_df_filtered)

        filtered_ride_to_job = filtered_ride[filtered_ride['Distance'] < 40] #TODO refactor this into input
        total_distance = filtered_ride_to_job['Distance'].sum()
        total_time = (filtered_ride_to_job['Elapsed Time'].sum()) / 3600
        data = [total_distance, total_time]
        return (data)

