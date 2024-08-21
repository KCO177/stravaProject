class Country:
    def __init__(self, country_name: str):
        self.value = self.validate_country_name(country_name)

    def validate_country_name(self, country_name: str) -> str:
        country_name_upper = country_name.upper().replace(" ", "_")
        # Iterate over the attributes of the Countries class
        country = next(
            (code for name, code in vars(Countries).items() if name == country_name_upper),
            None
        )
        if not country:
            raise ValueError(f"Country name {country_name} is not valid or supported")
        return country

class Countries:
    CZECH = "CZ"
    CESKA_REPUBLIKA = "CZ"
    ČESKÁ_REPUBLIKA = "CZ"
    ČESKO = "CZ"
    CZECHIA = "CZ"
    CZECH_REPUBLIC = "CZ"
    SLOVAKIA = "SK"
    HUNGARY = "HU"
    GERMANY = "DE"
