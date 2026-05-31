import pandas as pd

excel_file = r"D:\EPL_Portal\data\EPL.xlsx"

df = pd.read_excel(
    excel_file,
    sheet_name="FDD Cells"
)

for i, col in enumerate(df.columns):
    print(i, repr(col))