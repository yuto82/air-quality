
import os
from os.path import join, dirname
from dotenv import load_dotenv

env_path = join(dirname(__file__), "..", ".env")
load_dotenv(env_path)

class Config:
    WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")
    IQAIR_API_KEY = os.environ.get("IQAIR_API_KEY")
    
    CITY = "ioannina"
    STATE = "epirus"
    COUNTRY = "greece"
    START_DATE = "2024-09-19"
    END_DATE = "2024-09-20"