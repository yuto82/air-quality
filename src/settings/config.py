import os
from os.path import join, dirname
from dotenv import load_dotenv
from datetime import datetime

env_path = join(dirname(__file__), ".env")
load_dotenv(env_path)

class Config:
    WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")
    AIR_QUALITY_KEY = os.environ.get("AIR_QUALITY_KEY")
    
    LATITUDE = os.environ.get("LATITUDE")
    LONGITUDE = os.environ.get("LONGITUDE")
    
    START_DATE = os.environ.get("START_DATE")
    END_DATE = os.environ.get("END_DATE")

    START_DATE_UNIX = int(datetime.strptime(START_DATE, "%Y-%m-%d").timestamp())
    END_DATE_UNIX = int(datetime.strptime(END_DATE, "%Y-%m-%d").timestamp())

    DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data")