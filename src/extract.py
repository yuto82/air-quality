import json
from pathlib import Path
from settings.config import Config
from services.weather import extract_weather
from services.air_quality import extract_air_quality
from settings.utils import create_logger

logger = create_logger()

def main():
    api_key_weather = Config.WEATHER_API_KEY
    api_key_air = Config.AIR_QUALITY_KEY

    latitude = Config.LATITUDE
    longitude = Config.LONGITUDE

    start_date = Config.START_DATE
    end_date = Config.END_DATE

    start_date_unix = Config.START_DATE_UNIX
    end_date_unix = Config.END_DATE_UNIX

    data_path = Path(Config.DATA_PATH)
    
    weather_data = extract_weather(latitude, longitude, start_date, end_date, api_key_weather)
    air_quality_data = extract_air_quality(latitude, longitude, start_date_unix, end_date_unix, api_key_air)

    try:
        weather_file = data_path / "weather_data.json"
        with open(weather_file, "w") as file:
            json.dump(weather_data, file, indent=4)
        logger.info(f"Weather data saved successfully as {weather_file}")

        air_quality_file = data_path / "air_quality_data.json" 
        with open(air_quality_file, "w") as file:
            json.dump(air_quality_data, file, indent=4)
        logger.info(f"Air quality data saved successfully as {air_quality_file}")

    except Exception as e:
        logger.error(f"Failed to save data files: {e}")

if __name__ == "__main__":
    main()