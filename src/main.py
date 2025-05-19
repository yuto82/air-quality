import json

from config import Config
from weather import extract_weather

def main():
    api_key = Config.WEATHER_API_KEY

    city = Config.CITY
    start_date = Config.START_DATE
    end_date = Config.END_DATE

    weather_data = extract_weather(city, start_date, end_date, api_key)
    print(weather_data)