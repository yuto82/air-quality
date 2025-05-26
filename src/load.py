import sys
import pandas as pd
from pathlib import Path
from settings.config import Config
from settings.utils import create_logger
from sqlalchemy import create_engine,text

logger = create_logger()

def create_database_engine():
    try:
        engine = create_engine(Config.DATABASE_URL)

        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        logger.info("Database engine created successfully.")
        return(engine)
    
    except Exception as e:
        logger.error(f"Failed to create database engine: {e}")
        sys.exit(1)

def load_data(files):
    engine = create_database_engine()
    
    try:
        for file, table_name in files.items():
            data = pd.read_csv(file)
            data.to_sql(table_name, engine, if_exists='replace', index=False)
        logger.info("Data successfully loaded into the database.")

    except Exception as e:
        logger.error(f"Failed to load data into the database: {e}")
        sys.exit(1)

def main():
    data_path = Path(__file__).parent / "data"

    files = {
        data_path / "data.csv": "data",
        data_path / "transformed_data_air.csv": "air_pollution",
        data_path / "transformed_data_weather.csv": "weather",
    }

    load_data(files)

if __name__ == "__main__":
    main()