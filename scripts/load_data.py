import pandas as pd
from sqlalchemy import create_engine

# config
DB_USER = "postgres"
DB_PASSWORD = "postgresql123"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "churn_project"

# load data
df = pd.read_csv(r"C:\Customer Churn Pipeline\customer_churn_pipeline\data\Telco-Customer-Churn.csv")
df.columns = df.columns.str.lower()

# create engine
engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# load data ke PostgreSQL
df.to_sql(
    "raw_churn",
    engine,
    schema="churn_schema",
    if_exists="replace",  # replace biar gampang dev
    index=False
)

print("Data berhasil masuk ke PostgreSQL (table: raw_churn)")