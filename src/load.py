import pandas as pd
from pathlib import Path
from settings.config import Config
from sqlalchemy import create_engine

engine = create_engine(Config.DATABASE_URL)

df = pd.read_csv(Path(__file__).parent / "data" / "data.csv")
df.to_sql("weather_db", engine, if_exists='replace', index=False)