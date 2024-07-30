import pandas as pd

class data_strava:

    def strava_csv():
        strava_data = pd.read_csv('/export_109512466/activities.csv')
        df = pd.DataFrame(strava_data)
        strava_df_filtered = df[['Activity Date', 'Activity Type', 'Elapsed Time', 'Distance']]
        #print(strava_df_filtered)
        filtered_ride = strava_df_filtered[strava_df_filtered['Activity Type'].str.contains('Ride')]

        filtered_ride_to_job = filtered_ride[filtered_ride['Distance'] < 20]
        total_distance = filtered_ride_to_job['Distance'].sum()
        total_time = (filtered_ride_to_job['Elapsed Time'].sum()) / 3600


        #print(filtered_ride)
        print('total distance ', total_distance, 'time')
        print('total time elapsed ', total_time, 'hours')
        data = [total_distance, total_time]
        print(data[0])
        return (data)

data_strava.strava_csv()
