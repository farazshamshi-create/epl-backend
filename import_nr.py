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
    sheet_name="NR Cell"
)

df.columns = df.columns.str.strip()

nr = pd.DataFrame()

nr["cell_name"] = df["Cell Name"]
nr["site_id"] = df["Site ID"]
nr["cgi"] = df["CGI"].astype(str)

nr["pci"] = pd.to_numeric(
    df["PCI"],
    errors="coerce"
)

nr["azimuth"] = pd.to_numeric(
    df["Final Azimuth"],
    errors="coerce"
)

nr["height"] = pd.to_numeric(
    df["Height"],
    errors="coerce"
)

nr["mtilt"] = df["Mtilt"].astype(str)
nr["etilt"] = df["Etilt"].astype(str)

nr["power"] = pd.to_numeric(
    df["Antenna Pwr"],
    errors="coerce"
)

nr["onair"] = 1

with engine.begin() as conn:
    conn.exec_driver_sql(
        "TRUNCATE TABLE nr_cells RESTART IDENTITY"
    )

nr.to_sql(
    "nr_cells",
    engine,
    if_exists="append",
    index=False,
    chunksize=1000
)

print(f"Imported {len(nr)} NR records successfully")