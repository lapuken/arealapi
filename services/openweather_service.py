from typing import Optional


def get_report(city: str, state: Optional[str], country: str, units: str) ->dict:
    q = f'{city}, {state}, {country}'
    key = 123

    url = f'https://api.openweathermap.org/geo/1.0/direct?q={q}&appid={key}?units={units}'