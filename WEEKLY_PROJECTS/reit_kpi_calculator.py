# REIT KPI Calculator

print("=== REIT KPI CALCULATOR ===")

# User Inputs
reit_name = input("Enter REIT name: ")

property_value = float(input("Enter total property value: "))
debt = float(input("Enter total debt: "))
annual_dividend = float(input("Enter annual dividend per share: "))
share_price = float(input("Enter share price: "))
net_income = float(input("Enter net income: "))
total_assets = float(input("Enter total assets: "))
occupied_space = float(input("Enter occupied space: "))
total_space = float(input("Enter total lettable space: "))

# KPI Calculations
ltv_ratio = debt / property_value

dividend_yield = annual_dividend / share_price

roa = net_income / total_assets

occupancy_rate = occupied_space / total_space

# Results
print("\n=== RESULTS ===")

print(f"REIT: {reit_name}")

print(f"Loan-to-Value Ratio: {ltv_ratio:.2%}")

print(f"Dividend Yield: {dividend_yield:.2%}")

print(f"Return on Assets: {roa:.2%}")

print(f"Occupancy Rate: {occupancy_rate:.2%}")