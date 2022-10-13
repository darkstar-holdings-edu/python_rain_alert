import requests

from config import CONFIG

OPEN_WEATHER_API_KEY = CONFIG["openweather_api_key"]

API_ENDPOINT = "api.openweathermap.org"
SERVICE_ENDPOINT_MAP = {
    "location": {"protocol": "http", "endpoint": "geo/1.0"},
    "current_weather": {"protocol": "https", "endpoint": "data/2.5/weather"},
    "forecast": {"protocol": "https", "endpoint": "data/2.5/forecast"},
}


def build_url(type: str) -> str:
    map = SERVICE_ENDPOINT_MAP[type]
    return f"{map['protocol']}://{API_ENDPOINT}/{map['endpoint']}"


def send_request(url: str, params: dict) -> dict:
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    return data


def get_location(postal_code: str, country_code: str) -> tuple[int, int]:
    url = "/".join([build_url("location"), "zip"])
    params = {
        "zip": ",".join([postal_code, country_code]),
        "appid": OPEN_WEATHER_API_KEY,
    }

    data = send_request(url=url, params=params)

    return (data["lat"], data["lon"])


def get_current_weather(lat: int, lon: int) -> dict:
    params = {
        "lat": lat,
        "lon": lon,
        "appid": OPEN_WEATHER_API_KEY,
    }

    data = send_request(url=build_url("current_weather"), params=params)

    return data


def get_forecast(lat: int, lon: int) -> dict:
    params = {
        "lat": lat,
        "lon": lon,
        "cnt": 4,
        "appid": OPEN_WEATHER_API_KEY,
    }

    data = send_request(url=build_url("forecast"), params=params)

    return data


def is_rain_in_forecast(postal_code: str, country_code: str) -> bool:
    location = get_location(postal_code=postal_code, country_code=country_code)
    forecast = get_forecast(lat=location[0], lon=location[1])
    forecast_ids = [
        f["weather"][0]["id"] for f in forecast["list"] if f["weather"][0]["id"] < 700
    ]

    return True if len(forecast_ids) > 0 else False
