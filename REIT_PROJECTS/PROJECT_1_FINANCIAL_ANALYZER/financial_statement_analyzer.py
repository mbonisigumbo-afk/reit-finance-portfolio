import pandas as pd
from pathlib import Path

file_path = Path(__file__).parent / "reit_financials.csv"

print(file_path)

df = pd.read_csv(file_path)

print(df)
# Calculate ratios

df["ROA"] = (df["Net_Income"] / df["Total_Assets"]) * 100

df["Debt_to_Assets"] = (df["Debt"] / df["Total_Assets"]) * 100

df["Revenue_per_Asset"] = (df["Revenue"] / df["Total_Assets"]) * 100

# Sort by ROA
df = df.sort_values(by="ROA", ascending=False)

print("\n=== REIT FINANCIAL ANALYZER ===\n")

print(df)

def debt_risk_rating(debt_ratio):
    if debt_ratio < 35:
        return "LOW RISK"
    elif debt_ratio < 50:
        return "NORMAL"
    else:
        return "HIGH RISK"
    
df["Risk_Rating"] = df["Debt_to_Assets"].apply(debt_risk_rating)

print("\n=== REIT ANALYST SUMMARY ===\n")

for _, row in df.iterrows():
    print(
        f"{row['REIT']}: "
        f"ROA={row['ROA']:.2f}% | "
        f"Debt-to-Assets={row['Debt_to_Assets']:.2f}% | "
        f"Risk={row['Risk_Rating']}"
    )