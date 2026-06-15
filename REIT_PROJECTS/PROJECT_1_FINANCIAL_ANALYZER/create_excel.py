import pandas as pd
from pathlib import Path

project_folder = Path(__file__).parent

csv_file = project_folder / "reit_financials.csv"
excel_file = project_folder / "reit_financials_real.xlsx"

df = pd.read_csv(csv_file)

df.to_excel(
    excel_file,
    index=False
)

print("Excel workbook created successfully!")
print(excel_file)