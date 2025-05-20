import json

from config import Config
from weather import extract_weather
from air_quality import extract_air_quality

def main():
    api_key = Config.WEATHER_API_KEY
    api_key2 = Config.API_KEY

    latitude = Config.LATITUDE
    longtitude = Config.LONGTITUDE

    start_date = Config.START_DATE
    end_date = Config.END_DATE

    start_date_unix = Config.START_DATE_UNIX
    end_date_unix = Config.END_DATE_UNIX

    weather_data = extract_weather(latitude, longtitude, start_date, end_date, api_key)
    print(weather_data)

main()