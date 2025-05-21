import sys
import json
import pandas as pd
from pathlib import Path

def load_data(filename):
    try:
        file_path = Path(__file__).parent / "data" / filename

        with open(file_path, "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"File {filename} not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print("Error decoding JSON from the file.")
        sys.exit(1)

def transform_data(raw_data):

    records = raw_data.get("list", [])
    df = pd.json_normalize(records)

    df["dt"] = pd.to_datetime(df["dt"], unit = "s").dt.date

    df = df.groupby("dt")[
        ["main.aqi", 
        "components.pm2_5", 
        "components.pm10",
        "components.no", 
        "components.no2", 
        "components.o3",
        "components.co", 
        "components.so2", 
        "components.nh3"]].mean().reset_index()
    
    df.columns = ["date", "AQI", "PM25", "PM10", "NO", "NO2", "O3", "CO", "SO2", "NH3"]

    return df

if __name__ == "__main__":
    raw_data = load_data("air_quality_data.json")
    df_daily = transform_data(raw_data)

    df_daily.to_csv("transformed_data_air.csv", index=False)
