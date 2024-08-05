class Car:
    class City:
        small = (7.8, 9.4)
        medium = (9.4, 11.8)
        small_SUV = (9.4, 11.8)
        SUV = (11.8, 15.7)

    class CombinedRoad:
        small = (6.7, 7.8)
        medium = (7.8, 9.4)
        small_SUV = (8.7, 10.7)
        SUV = (10.7, 13.1)

    class Highway:
        small = (5.9, 6.7)
        medium = (6.7, 7.8)
        small_SUV = (7.8, 9.4)
        SUV = (9.4, 11.8)

    def get_value_from_range(self, car_type, category, percentage):
        if hasattr(Car, category):
            cat_class = getattr(Car, category)
            if hasattr(cat_class, car_type):
                value_range = getattr(cat_class, car_type)
                min_val, max_val = value_range
                value = min_val + (max_val - min_val) * (percentage / 100)
                return value
        raise ValueError("Invalid category or car type")



