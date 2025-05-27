# Weather and Air Quality ETL Pipeline

## Overview
This project implements an ETL (Extract, Transform, Load) pipeline for collecting and processing historical weather and air pollution data for a specified location.
The pipeline fetches data from external APIs, transforms it into a clean and structured tabular format, and then loads the processed data into a database.
The goal of this project is to provide a robust and well-transformed dataset that can be used for further analysis, visualization and reporting.

## Technologies Used

- **Programming language:** 
  - Python 3.13.3
- **Database:** 
  - PostgreSQL 14.17
- **Python Libraries:**
  - pandas 2.2.3
  - requests 2.32.3
  - SQLAlchemy 2.0.41
  - numpy 2.2.6
  - dotenv 1.1.0
- **Data Sources:**
  - [Weather API](https://www.visualcrossing.com/weather-api/)
  - [Air Pollution API](https://openweathermap.org/api)

## Project Structure
```
├── src/
│   ├── extract.py                 # Extracting data from APIs
│   ├── transform.py               # Transforms extracted data
│   ├── load.py                    # Loading transformed data into database
│   ├── services/                  # Fetching logic module
│   │   ├── air_quality.py         # Fetch air quality data
│   │   └── weather.py             # Fetch weather data
│   └── settings/                  # Directory with configuration and utility functions
│   │   ├── config.py              # Configuration for API keys and URLs
│   │   └── utils.py               # Functions used across the project
│   ├── data/                      # Directory which holds processed data
├── README.md                      # Project documentation
├── requirements.txt               # List of Python dependencies
└── run.sh                         # Execute the ETL pipeline
```
## ETL Pipeline Breakdown
This project implements an ETL (Extract, Transform, Load) pipeline for collecting and processing data from external APIs. The pipeline consists of the following main steps:

### 1. Extract
- **Modules:** `extract.py`, `air_quality.py`, `weather.py`.
- **Description:** Data collected using [Visual Crossing Weather](https://www.visualcrossing.com/weather-api/) and [OpenWeatherAPI](https://openweathermap.org/api). Weather data includes temperature, feels like temperature, humidity, pressure and wind speed. Air Pollution data includes AQI, PM25, PM10, NO, NO2, O3, CO, SO2, NH3.
- **Output:** JSON files stored in `data/` directory: `weather_data.json`, `air_quality_data.json`.

### 2. Transform
- **Modules:** `transform.py`
- **Description:** Clean, normalize, and reshape raw data into tabular format suitable for analysis.
- **Output:** CSV files stored in `data/` directory: `data.csv`, `transformed_data_air.csv`, `transformed_data_weather.csv`.

### 3. Load
- **Modules:** `load.py`
- **Description:** The cleaned and transformed data is stored in PostgreSQL. Database includes separate tables for weather, air pollution, and merged data.
- **Output:** Data is inserted into the following PostgreSQL tables: `data`, `weather`, `air_pollution`. 

## How to Run the Project

### 1. Prerequisites
Before running the ETL pipeline, make sure you have the following installed:
- Python (version 3.8+) 
- PostgreSQL (version 9.6+) with database and user access.
- [OpenWeatherAPI](https://openweathermap.org/api) and [Visual Crossing Weather](https://www.visualcrossing.com/weather-api/) API keys.

### 2. Setup Instructions
#### 1. Clone the repository:
```
git clone https://github.com/yuto82/weather_air-quality.git
cd weather_air-quality
```

#### 2. Create and activate a virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install the required dependencies:
```
pip install -r requirements.txt
```

#### 4. Set up the environment variables:
```
WEATHER_API_KEY=
WEATHER_API_KEY=
AIR_QUALITY_KEY=
LATITUDE=
LONGITUDE=
START_DATE=
END_DATE=
DATABASE_URL=postgresql://<username>:<password>@<host>:<port>/<database>
```