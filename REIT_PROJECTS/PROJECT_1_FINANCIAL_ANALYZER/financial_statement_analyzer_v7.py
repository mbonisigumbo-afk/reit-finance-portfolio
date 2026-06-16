import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

def load_data():

    file_path = (
        Path(__file__).parent
        / "reit_financials_real.xlsx"
    )

    try:
        df = pd.read_excel(file_path)
        return df

    except FileNotFoundError:
        print("Financial file not found.")
        exit()

def validate_data(df):

    if (df["Revenue"] < 0).any():
        print("WARNING: Negative revenue detected")

    if (df["Total_Assets"] <= 0).any():
        print("WARNING: Invalid asset values detected")

def calculate_ratios(df):

    df["ROA"] = (
        df["Net_Income"]
        / df["Total_Assets"]
    ) * 100

    df["Debt_to_Assets"] = (
        df["Debt"]
        / df["Total_Assets"]
    ) * 100

    df["Revenue_per_Asset"] = (
        df["Revenue"]
        / df["Total_Assets"]
    ) * 100

    return df

def debt_risk_rating(debt_ratio):

    if debt_ratio < 35:
        return "LOW RISK"

    elif debt_ratio < 50:
        return "NORMAL"

    else:
        return "HIGH RISK"

def generate_summary(df):

    print("\n=== REIT ANALYST SUMMARY ===\n")

    for _, row in df.iterrows():

        print(
            f"Rank #{row['ROA_Rank']} | "
            f"{row['REIT']} | "
            f"ROA={row['ROA']:.2f}% | "
            f"Debt={row['Debt_to_Assets']:.2f}% | "
            f"Risk={row['Risk_Rating']}"
        )

def portfolio_statistics(df):

    print("\n=== PORTFOLIO STATISTICS ===\n")

    print(
        f"Average ROA: "
        f"{df['ROA'].mean():.2f}%"
    )

    print(
        f"Average Debt Ratio: "
        f"{df['Debt_to_Assets'].mean():.2f}%"
    )

    print(
        f"Total Assets: "
        f"R{df['Total_Assets'].sum():,.0f}"
    )

def create_roa_chart(df):

    plt.figure()

    plt.bar(
        df["REIT"],
        df["ROA"]
    )

    plt.title("ROA by REIT")
    plt.ylabel("ROA (%)")

    plt.savefig("roa_chart.png")
    plt.close()


def create_debt_chart(df):

    plt.figure()

    plt.bar(
        df["REIT"],
        df["Debt_to_Assets"]
    )

    plt.title("Debt-to-Assets by REIT")
    plt.ylabel("Debt Ratio (%)")

    plt.savefig("debt_chart.png")
    plt.close()

def create_revenue_efficiency_chart(df):

    plt.figure()

    plt.bar(
        df["REIT"],
        df["Revenue_per_Asset"]
    )

    plt.title("Revenue per Asset by REIT")
    plt.ylabel("Revenue per Asset (%)")

    plt.savefig("revenue_efficiency_chart.png")
    plt.close()

def main():

    df = load_data()

    validate_data(df)

    df = calculate_ratios(df)

    df["Risk_Rating"] = (
        df["Debt_to_Assets"]
        .apply(debt_risk_rating)
    )

    df["ROA_Rank"] = (
        df["ROA"]
        .rank(
            ascending=False,
            method="dense"
        )
        .astype(int)
    )

    df = df.sort_values(
        by="ROA",
        ascending=False
    )

    generate_summary(df)

    best_reit = df.loc[df["ROA"].idxmax()]

    print("\n=== TOP PERFORMER ===\n")

    print(
    f"{best_reit['REIT']} has the highest ROA "
    f"at {best_reit['ROA']:.2f}%"
)

    portfolio_statistics(df)

    print("\n=== DASHBOARD METRICS ===\n")

    print(
        f"Highest ROA: "
        f"{df.loc[df['ROA'].idxmax(), 'REIT']}"
    )

    print(
        f"Lowest Debt Ratio: "
        f"{df.loc[df['Debt_to_Assets'].idxmin(), 'REIT']}"
    )

    print(
        f"Best Revenue Efficiency: "
        f"{df.loc[df['Revenue_per_Asset'].idxmax(), 'REIT']}"
    )

    create_roa_chart(df)
    create_debt_chart(df)
    create_revenue_efficiency_chart(df)

    output_file = (
        Path(__file__).parent
        / "reit_analysis_output.xlsx"
    )

    df.to_excel(
        output_file,
        index=False
    )

    print("\nExcel report created.")

if __name__ == "__main__":
    main()

