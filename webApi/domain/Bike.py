class Bike:

    roadBikeEasy = 400
    roadBikeModerate = 550
    roadBikeIntense = 700
    gravelBikeEasy = 450
    gravelBikeModerate = 600
    gravelBikeIntense = 750
    mountainBikeEasy = 500
    mountainBikeModerate = 650
    mountainBikeIntense = 800

    def get_bike_value(bike_type: str) -> int:
        # Ensure the attribute exists in the Bike class
        if hasattr(Bike, bike_type):
            return getattr(Bike, bike_type)
        else:
            raise ValueError(f"Attribute {bike_type} not found in Bike class")

