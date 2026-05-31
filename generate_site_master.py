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

# Read LTE sheet
lte = pd.read_excel(
    excel_file,
    sheet_name="FDD Cells"
)

lte.columns = lte.columns.str.strip()

site_master = lte[
    [
        "Site ID",
        "OLD Site ID",
        "LATITUDE",
        "Longitude",
        "Region",
        "Area"
    ]
].copy()

site_master = site_master.drop_duplicates(
    subset=["Site ID"]
)

site_master.columns = [
    "site_id",
    "old_site_id",
    "latitude",
    "longitude",
    "region",
    "area"
]

site_master["site_type"] = None
site_master["status"] = "ONAIR"

with engine.begin() as conn:
    conn.exec_driver_sql(
        "TRUNCATE TABLE site_master"
    )

site_master.to_sql(
    "site_master",
    engine,
    if_exists="append",
    index=False
)

print(
    f"Imported {len(site_master)} sites successfully"
)