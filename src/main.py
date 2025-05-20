import json
import requests
from config import Config
from weather import extract_weather
from air_quality import extract_air_quality

def main():
    api_key_weather = Config.WEATHER_API_KEY
    api_key_air = Config.AIR_QUALITY_KEY

    latitude = Config.LATITUDE
    longtitude = Config.LONGTITUDE

    start_date = Config.START_DATE
    end_date = Config.END_DATE

    start_date_unix = Config.START_DATE_UNIX
    end_date_unix = Config.END_DATE_UNIX

    weather_data = extract_weather(latitude, longtitude, start_date, end_date, api_key_weather)
    print(weather_data)

    air_quality_data = extract_air_quality(latitude, longtitude, start_date_unix, end_date_unix, api_key_air)
    print(air_quality_data)

main()