import pandas as pd
from sqlalchemy import create_engine

DB_USER = "postgres"
DB_PASSWORD = "faraz9024"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "epl_portal"

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

excel_file = r"D:\EPL_Portal\data\EPL.xlsx"

df = pd.read_excel(
    excel_file,
    sheet_name="TDD 2.6"
)

df.columns = df.columns.str.strip()

l2600 = pd.DataFrame()

l2600["cell_name"] = df["Cell Name"]
l2600["site_id"] = df["Site ID"]
l2600["cgi"] = df["CGI"].astype(str)
l2600["pci"] = df["Code"]
l2600["arfcn"] = df["ARFCN"]
l2600["azimuth"] = df["Azimuth"]
l2600["height"] = df["Antheight"]
l2600["mtilt"] = df["Mtilt"].astype(str)
l2600["etilt"] = df["Etilt"].astype(str)
l2600["onair"] = df["Onair Status"]

with engine.begin() as conn:
    conn.exec_driver_sql(
        "TRUNCATE TABLE l2600_cells RESTART IDENTITY"
    )

l2600.to_sql(
    "l2600_cells",
    engine,
    if_exists="append",
    index=False,
    chunksize=1000
)

print(f"Imported {len(l2600)} L2600 records successfully")