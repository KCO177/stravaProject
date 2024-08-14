class DataFilter():
    def filterRides(activities):
        filteredRides = [activity for activity in activities if activity['type'] == 'Ride']
        return filteredRides

    def filterCountry(athlete):
        country = athlete.get("country")
        return country


