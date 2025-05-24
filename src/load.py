import sys
import pandas as pd
from pathlib import Path
from settings.config import Config
from sqlalchemy import create_engine,text

def create_db_engine():
    try:
        engine = create_engine(Config.DATABASE_URL)

        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        print(f"Engine created successfully!")

        return(engine)
    
    except Exception as e:
        print(f"Error creating engine: {e}")
        sys.exit(1)

def load_db_data(files):
    engine = create_db_engine()
    
    try:
        for file, table_name in files.items():
            data = pd.read_csv(file)
            data.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"Data loaded into the table successfully!")

    except Exception as e:
        print(f"Error loading data to PostgreSQL: {e}")
        sys.exit(1)

def drop_tables(tables):
    engine = create_db_engine()
    try:
        with engine.begin() as conn:
            for table_name in tables:
                conn.execute(text(f'DROP TABLE IF EXISTS "{table_name}" CASCADE'))
            print(f"Tables deleted successfully!")
    except Exception as e:
        print(f"Error deleting tables: {e}")
        sys.exit(1)

def main():
    data_path = Path(__file__).parent / "data"

    files = {
        data_path / "data.csv": "data",
        data_path / "transformed_data_air.csv": "air_pollution",
        data_path / "transformed_data_weather.csv": "weather",
    }

    load_db_data(files)
    # drop_tables(files.values())

if __name__ == "__main__":
    main()