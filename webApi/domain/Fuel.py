class Fuel:
    E95 = 2390
    B7 = 2640
    LPG = 1700
    CNG = 2000

    def get_fuel_data(self, fuelInput, price):
        if len(fuelInput) > 3:
            print("Fuel input is too long.")
            return None, None

        # Get the first letter of the fuel input
        letter = fuelInput[0].upper()

        # Dictionary mapping letters to Fuel class attributes and price indices
        fuel_mapping = {
            'E': (Fuel.E95, 2),
            'B': (Fuel.B7, 3)
            # 'L': (Fuel.LPG, 4), not supported price yet
            # 'C': (Fuel.CNG, 5), not supported price yet
        }

        # Get the CO2 emission and price index from the dictionary
        if letter in fuel_mapping:
            litr_fuel, price_index = fuel_mapping[letter]
            price_fuel = float(price.getValidPrices()[price_index])
        else:
            print("Not supported fuel yet.")
            litr_fuel = None
            price_fuel = None

        return litr_fuel, price_fuel

