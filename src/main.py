import json

from config import Config
from weather import extract_weather
from air_quality import extract_air_quality

def main():
    api_key = Config.WEATHER_API_KEY
    api_key2 = Config.IQAIR_API_KEY

    city = Config.CITY
    state = Config.STATE
    country = Config.COUNTRY

    start_date = Config.START_DATE
    end_date = Config.END_DATE

    weather_data = extract_air_quality(city, state, country, start_date, end_date, api_key2)
    print(weather_data)

main()