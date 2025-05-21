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

def transform_data(weather_data):

    hourly_data = [
        {**hour, "date": day.get("datetime", None)}
        for day in weather_data.get("days", [])
        for hour in day.get("hours", [])
    ]

    df = pd.DataFrame(hourly_data)
    df = df[["date", "datetime", "temp", "feelslike", "humidity", "pressure"]]
    print(df)


if __name__ == "__main__":
    raw_data = load_data("weather_data.json")
    df_hourly = transform_data(raw_data)