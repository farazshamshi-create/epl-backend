import pandas as pd

excel_file = r"D:\EPL_Portal\data\EPL.xlsx"

xls = pd.ExcelFile(excel_file)

print(xls.sheet_names)