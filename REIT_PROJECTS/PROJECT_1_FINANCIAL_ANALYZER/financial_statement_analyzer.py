import pandas as pd
from pathlib import Path

file_path = Path(__file__).parent / "reit_financials.csv"

print(file_path)

df = pd.read_csv(file_path)

print(df)
# Calculate ratios

df["ROA"] = df["Net_Income"] / df["Total_Assets"]

df["Debt_to_Assets"] = df["Debt"] / df["Total_Assets"]

df["Revenue_per_Asset"] = df["Revenue"] / df["Total_Assets"]

# Sort by ROA
df = df.sort_values(by="ROA", ascending=False)

print("\n=== REIT FINANCIAL ANALYZER ===\n")

print(df)