import sys
import requests

def extract_weather(latitude, longtitude, start_date, end_date, api_key):
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{latitude},{longtitude}/{start_date}/{end_date}?unitGroup=metric&key={api_key}&contentType=json"

    try:
        response = requests.get(url)

        response.raise_for_status()

        weather_data = response.json()
        return(weather_data)
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        sys.exit(1)

    except Exception as err:
        print(f"An error occurred: {err}")
        sys.exit(1)

