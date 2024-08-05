class Distance:
    def get_sum_of_km(self, filteredRides):
        km = int(filteredRides['Distance'].sum()) / 1000
        return km
