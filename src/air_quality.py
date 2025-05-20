import sys
import requests

def extract_air_quality(city, state, country, start_date, end_date, api_key):
    url = (f"https://api.airvisual.com/v2/history?city={city}&state={state}&country={country}"
           f"&start={start_date}&end={end_date}&key={api_key}")

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

