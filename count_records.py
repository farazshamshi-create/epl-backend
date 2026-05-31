import pandas as pd

excel_file = r"D:\EPL_Portal\data\EPL.xlsx"

lte = pd.read_excel(
    excel_file,
    sheet_name="FDD Cells"
)

l2600 = pd.read_excel(
    excel_file,
    sheet_name="TDD 2.6"
)

nr = pd.read_excel(
    excel_file,
    sheet_name="NR Cell"
)

print("\n===== EPL SUMMARY =====")

print(f"LTE Cells    : {len(lte)}")
print(f"L2600 Cells  : {len(l2600)}")
print(f"NR Cells     : {len(nr)}")

all_sites = set()

all_sites.update(lte["Site ID"].dropna().astype(str))
all_sites.update(l2600["Site ID"].dropna().astype(str))
all_sites.update(nr["Site ID"].dropna().astype(str))

print(f"Total Sites  : {len(all_sites)}")