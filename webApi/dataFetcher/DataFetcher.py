import requests

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

def filterCyclingActivity():
    return list#cycling activities

def getRoute(): #TODO get km from route
    return #km


