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