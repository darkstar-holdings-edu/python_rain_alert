from openweather_api import is_rain_in_forecast


def main() -> None:
    if is_rain_in_forecast(postal_code="92336", country_code="US"):
        print("Rain is forecasted")
    else:
        print("Rain is not forecasted")


if __name__ == "__main__":
    main()
