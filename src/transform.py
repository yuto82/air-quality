import sys
import json
import pandas as pd
from pathlib import Path
from settings.utils import create_logger

logger = create_logger()

def load_data(filename):
    try:
        file_path = Path(__file__).parent / "data" / filename

        with open(file_path, "r") as file:
            data = json.load(file)
        logger.info(f"Successfully loaded data from {filename}")
        return(data)
    
    except FileNotFoundError:
        logger.error(f"File {filename} not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        logger.error(f"Error decoding JSON from {filename}.")
        sys.exit(1)

def transform_weather(raw_data):
    logger.info("Transforming air quality data")
    records = raw_data.get("days", [])
    logger.info(f"Records received: {len(records)}")

    df = pd.DataFrame(records)

    df = df[["datetime", "temp", "feelslike", "humidity", "pressure", "windspeed"]]
    df.columns = ["date", "temperature", "feels_like", "humidity", "pressure", "wind_speed"]

    df["date"] = pd.to_datetime(df["date"])
    df["temperature"] = pd.to_numeric(df["temperature"], errors="coerce").round(1)
    df["feels_like"] = pd.to_numeric(df["feels_like"], errors="coerce").round(1)
    df["humidity"] = pd.to_numeric(df["humidity"], errors="coerce").round(1)
    df["pressure"] = pd.to_numeric(df["pressure"], errors="coerce").round(1)
    df["wind_speed"] = pd.to_numeric(df["wind_speed"], errors="coerce").round(1)

    logger.info("Weather data transformation complete")
    return(df)

def transform_air_quality(raw_data):
    logger.info("Transforming air quality data")
    records = raw_data.get("list", [])
    logger.info(f"Records received: {len(records)}")

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

    df["AQI"] = pd.to_numeric(df["AQI"], errors="coerce").round(2)
    df["PM25"] = pd.to_numeric(df["PM25"], errors="coerce").round(1)
    df["PM10"] = pd.to_numeric(df["PM10"], errors="coerce").round(1)
    df["NO"] = pd.to_numeric(df["NO"], errors="coerce").round(1)
    df["NO2"] = pd.to_numeric(df["NO2"], errors="coerce").round(1)
    df["O3"] = pd.to_numeric(df["O3"], errors="coerce").round(1)
    df["CO"] = pd.to_numeric(df["CO"], errors="coerce").round(1)
    df["SO2"] = pd.to_numeric(df["SO2"], errors="coerce").round(1)
    df["NH3"] = pd.to_numeric(df["NH3"], errors="coerce").round(1)

    logger.info("Air quality data transformation complete")
    return df

def main():
    logger.info("Starting data processing")
    
    air_quality_raw = load_data("air_quality_data.json")
    df_air_quality = transform_air_quality(air_quality_raw)

    weather_raw = load_data("weather_data.json")
    df_weather = transform_weather(weather_raw)

    weather_path = Path(__file__).parent / "data" / "transformed_data_weather.csv"
    df_weather.to_csv(weather_path, index=False)
    logger.info(f"Weather data saved to {weather_path}")

    air_quality_path = Path(__file__).parent / "data" / "transformed_data_air.csv"
    df_air_quality.to_csv(air_quality_path, index=False)
    logger.info(f"Air quality data saved to {air_quality_path}")

    df_a = pd.read_csv(air_quality_path)
    df_w = pd.read_csv(weather_path)

    df_merged = pd.merge(df_a, df_w, on="date", how="inner")

    merged_path = Path(__file__).parent / "data" / "data.csv"
    df_merged.to_csv(merged_path, index=False)
    
    logger.info(f"Merged data saved to {merged_path}")
    logger.info(f"Final dataset shape: {df_merged.shape}")


if __name__ == "__main__":
    main()