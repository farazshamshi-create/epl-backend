import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL
DB_USER = "postgres"
DB_PASSWORD = "faraz9024"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "epl_portal"

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

excel_file = r"D:\EPL_Portal\data\EPL.xlsx"

# Read LTE Sheet
lte = pd.read_excel(
    excel_file,
    sheet_name="FDD Cells"
)

lte.columns = lte.columns.str.strip()



# Select required columns
lte_db = pd.DataFrame()

lte_db["cell_name"] = lte["Cell Name"]
lte_db["site_id"] = lte["Site ID"]
lte_db["tech_frequency"] = lte["Tech_Frequency"]
lte_db["pci"] = lte["Code"]

lte_db["cgi"] = lte["CGI"].astype(str)
lte_db["ci"] = lte["CI"]
lte_db["arfcn"] = lte["ARFCN"]
lte_db["azimuth"] = lte["Azimuth"]
lte_db["antheight"] = lte["ANTHEIGHT"]
lte_db["mtilt"] = lte["MTILT"].astype(str)
lte_db["etilt"] = lte["ETILT"].astype(str)
lte_db["onair"] = lte["ONAIR"]

# Clear existing data
with engine.begin() as conn:
    conn.exec_driver_sql("TRUNCATE TABLE lte_cells RESTART IDENTITY")

# Insert
lte_db.to_sql(
    "lte_cells",
    engine,
    if_exists="append",
    index=False,
    chunksize=1000
)

print(f"Imported {len(lte_db)} LTE records successfully")