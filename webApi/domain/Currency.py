import pycountry

from webApi.domain.Athlete import Athlete
from webApi.domain.Country import Country


class Currency:

    def get_currency_for_athlete(clientId):
        country = Athlete.getAthleteCountry(clientId)
        country_code = Country(country)
        country_code = country_code.value
        currency_code = Currency.get_currency_by_country_code(country_code)
        supported_currency = ['CZK'] #TODO replace with transform currencies
        if str(currency_code) in supported_currency:
            return currency_code
        else:
            raise ValueError(f"Currency {currency_code} is not supported")

    def get_currency_by_country_code(country_code: str):
        try:
            country = pycountry.countries.get(alpha_2=country_code.upper())
            if country:
                currency = pycountry.currencies.get(numeric=country.numeric)
                return currency.alpha_3
            else:
                raise ValueError(f"Country code {country_code} is not valid or supported")
        except Exception as e:
            return str(e)



