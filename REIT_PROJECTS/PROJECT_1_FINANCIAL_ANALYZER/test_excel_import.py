from pathlib import Path
import pandas as pd

file_path = Path(__file__).parent / "reit_financials_real.xlsx"

print("Loading:", file_path)

df = pd.read_excel(file_path)

print("\nExcel file loaded successfully!\n")
print(df)

from pathlib import Path
import pandas as pd