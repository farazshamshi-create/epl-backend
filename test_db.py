from sqlalchemy import create_engine
import pandas as pd

DB_USER = "postgres"
DB_PASSWORD = "faraz9024"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "epl_portal"

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

query = """
SELECT table_name
FROM information_schema.tables
WHERE table_schema='public';
"""

df = pd.read_sql(query, engine)

print(df)