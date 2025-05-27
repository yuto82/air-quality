import sys
import requests
from settings.utils import create_logger

logger = create_logger()

def extract_air_quality(latitude, longtitude, start_date, end_date, api_key):
    url = f"http://api.openweathermap.org/data/2.5/air_pollution/history?lat={latitude}&lon={longtitude}&start={start_date}&end={end_date}&appid={api_key}"

    try:
        response = requests.get(url)

        response.raise_for_status()

        weather_data = response.json()
        logger.info("Air quality data received successfully")
        return(weather_data)
    
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
        sys.exit(1)

    except Exception as err:
        logger.error(f"Unexpected error occurred: {err}")
        sys.exit(1)