import json
from pathlib import Path
from config import Config
from api_requests.weather import extract_weather
from api_requests.air_quality import extract_air_quality

def main():
    api_key_weather = Config.WEATHER_API_KEY
    api_key_air = Config.AIR_QUALITY_KEY

    latitude = Config.LATITUDE
    longtitude = Config.LONGTITUDE

    start_date = Config.START_DATE
    end_date = Config.END_DATE

    start_date_unix = Config.START_DATE_UNIX
    end_date_unix = Config.END_DATE_UNIX

    data_path = Path(Config.DATA_PATH)

    weather_data = extract_weather(latitude, longtitude, start_date, end_date, api_key_weather)
    air_quality_data = extract_air_quality(latitude, longtitude, start_date_unix, end_date_unix, api_key_air)

    with open(data_path / "weather_data.json", "w") as file:
        json.dump(weather_data, file, indent=4)

    with open(data_path / "air_quality_data.json", "w") as file:
        json.dump(air_quality_data, file, indent=4)

main()