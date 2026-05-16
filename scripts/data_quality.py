import pandas as pd
import sys

def check_data_quality(filepath):
    try:
        df = pd.read_csv(filepath)
    except pd.errors.EmptyDataError:
        print("FAIL: File is empty or has no columns")
        sys.exit(1)

    errors = []

    if df.empty:
        errors.append("FAIL: Dataframe is empty")

    required_cols = ["tenure", "MonthlyCharges", "TotalCharges", "Churn"]
    for col in required_cols:
        if col not in df.columns:
            errors.append(f"FAIL: Missing column '{col}'")

    for col in required_cols:
        if col in df.columns and df[col].isnull().sum() > 0:
            errors.append(f"FAIL: Nulls found in column '{col}'")

    if "Churn" in df.columns:
        valid_values = set(df["Churn"].unique())
        if not valid_values.issubset({0, 1}):
            errors.append(f"FAIL: Invalid Churn values: {valid_values}")

    if "MonthlyCharges" in df.columns:
        if (df["MonthlyCharges"] < 0).any():
            errors.append("FAIL: Negative MonthlyCharges found")

    if errors:
        for e in errors:
            print(e)
        sys.exit(1)
    else:
        print("All data quality checks passed!")
        return True

if __name__ == "__main__":
    check_data_quality("data/cleaned_churn.csv")
    



