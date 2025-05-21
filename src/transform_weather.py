import sys
import json
import pandas as pd
from pathlib import Path

def load_data(filename):
    try:
        file_path = Path(__file__).parent / "data" / filename

        with open(file_path, "r") as file:
            data = json.load(file)
        return(data)
    
    except FileNotFoundError:
        print.error(f"File {filename} not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print.error("Error decoding JSON from the file.")
        sys.exit(1)    

def transform_data(raw_weather_data):

    records = raw_weather_data.get("days", [])

    df = pd.DataFrame(records)

    df = df[["datetime", "temp", "feelslike", "humidity", "pressure", "windspeed"]]
    df.columns = ["date", "temperature", "feels_like", "humidity", "pressure", "wind_speed"]

    df["date"] = pd.to_datetime(df["date"])
    df["temperature"] = pd.to_numeric(df["temperature"], errors="coerce")
    df["feels_like"] = pd.to_numeric(df["feels_like"], errors="coerce")
    df["humidity"] = pd.to_numeric(df["humidity"], errors="coerce")
    df["pressure"] = pd.to_numeric(df["pressure"], errors="coerce")
    df["wind_speed"] = pd.to_numeric(df["wind_speed"], errors="coerce")

    return(df)

if __name__ == "__main__":
    raw_data = load_data("weather_data.json")
    df_hourly = transform_data(raw_data)

    df_hourly.to_csv("transformed_data.csv", index=False)