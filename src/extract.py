import requests

from config import Config

url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Tokyo/2020-10-19/2020-10-20?key={Config.WEATHER_API_KEY}"

response = requests.get(url)

weather_data = response.json()
print(weather_data)