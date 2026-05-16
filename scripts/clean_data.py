import pandas as pd

df = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Fix TotalCharges - it's a string, convert to number
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

# Fill missing TotalCharges with 0
df["TotalCharges"] = df["TotalCharges"].fillna(0)

# Drop customerID - not useful for prediction
df = df.drop(columns=["customerID"])

# Convert Churn Yes/No to 1/0
df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

print("Cleaned shape:", df.shape)
print("Missing values:", df.isnull().sum().sum())
print(df.head())

# Save cleaned data
df.to_csv("data/cleaned_churn.csv", index=False)
print("Saved cleaned data!")

from sklearn.preprocessing import LabelEncoder

# Get all object (text) columns except target
cat_cols = df.select_dtypes(include="object").columns.tolist()
print("Categorical columns:", cat_cols)

le = LabelEncoder()
for col in cat_cols:
    df[col] = le.fit_transform(df[col])

df.to_csv("data/encoded_churn.csv", index=False)
print("Encoding done! Saved to data/encoded_churn.csv")

