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

def load_db_data(data):
    engine = create_db_engine()

    try:
        data.to_sql("weather_data", engine, if_exists='replace', index=False)
        print(f"Data loaded into the table successfully!")

    except Exception as e:
        print(f"Error loading data to PostgreSQL: {e}")
        sys.exit(1)

def main():
    data_path = Path(__file__).parent / "data" / "data.csv"
    data = pd.read_csv(data_path)

    load_db_data(data)

if __name__ == "__main__":
    main()