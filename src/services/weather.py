import sys
import requests
from settings.utils import create_logger

logger = create_logger()

def extract_weather(latitude, longtitude, start_date, end_date, api_key):
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{latitude},{longtitude}/{start_date}/{end_date}?unitGroup=metric&key={api_key}&contentType=json"

    try:
        response = requests.get(url)

        response.raise_for_status()

        weather_data = response.json()
        logger.info("Weather data received successfully.")
        return(weather_data)
    
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
        sys.exit(1)

    except Exception as err:
        logger.error(f"Unexpected error occurred: {err}")
        sys.exit(1)