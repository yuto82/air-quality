
import os
from os.path import join, dirname
from dotenv import load_dotenv

env_path = join(dirname(__file__), "..", ".env")
load_dotenv(env_path)

class Config:
    WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")

