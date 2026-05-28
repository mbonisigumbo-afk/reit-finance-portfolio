# REIT KPI Calculator V2

print("=== REIT KPI CALCULATOR V2 ===")


# FUNCTIONS
def calculate_ltv(debt, property_value):
    return debt / property_value


def calculate_dividend_yield(dividend, share_price):
    return dividend / share_price


def calculate_roa(net_income, total_assets):
    return net_income / total_assets


def calculate_occupancy(occupied_space, total_space):
    return occupied_space / total_space


def calculate_interest_cover(ebit, interest_expense):
    return ebit / interest_expense


# USER INPUTS
reit_name = input("Enter REIT name: ")

property_value = float(input("Enter total property value: "))
debt = float(input("Enter total debt: "))
annual_dividend = float(input("Enter annual dividend per share: "))
share_price = float(input("Enter share price: "))
net_income = float(input("Enter net income: "))
total_assets = float(input("Enter total assets: "))
occupied_space = float(input("Enter occupied space: "))
total_space = float(input("Enter total lettable space: "))
ebit = float(input("Enter EBIT: "))
interest_expense = float(input("Enter interest expense: "))


# CALCULATIONS
ltv_ratio = calculate_ltv(debt, property_value)

dividend_yield = calculate_dividend_yield(
    annual_dividend,
    share_price
)

roa = calculate_roa(net_income, total_assets)

occupancy_rate = calculate_occupancy(
    occupied_space,
    total_space
)


interest_cover = calculate_interest_cover(
    ebit,
    interest_expense
)


# RESULTS
print("\n=== RESULTS ===")

print(f"\nREIT: {reit_name}")

print(f"Loan-to-Value Ratio: {ltv_ratio:.2%}")

print(f"Dividend Yield: {dividend_yield:.2%}")

print(f"Return on Assets: {roa:.2%}")

print(f"Occupancy Rate: {occupancy_rate:.2%}")

print(f"Interest Coverage Ratio: {interest_cover:.2f}")