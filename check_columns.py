import pandas as pd

excel_file = r"D:\EPL_Portal\data\EPL.xlsx"

for sheet in ["FDD Cells", "TDD 2.6", "NR Cell"]:

    df = pd.read_excel(
        excel_file,
        sheet_name=sheet,
        nrows=1
    )

    print("\n")
    print("=" * 80)
    print(sheet)
    print("=" * 80)

    for col in df.columns:
        print(col)