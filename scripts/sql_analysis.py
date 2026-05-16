import pandas as pd
import sqlite3

df = pd.read_csv("data/cleaned_churn.csv")

conn = sqlite3.connect("data/churn.db")
df.to_sql("customers", conn, if_exists="replace", index=False)
print("Data loaded into SQLite!")

# Average monthly charges by churn
query1 = """
SELECT 
    Churn,
    COUNT(*) AS customer_count,
    ROUND(AVG(MonthlyCharges), 2) AS avg_monthly_charges,
    ROUND(AVG(tenure), 2) AS avg_tenure_months
FROM customers
GROUP BY Churn
"""
print(pd.read_sql(query1, conn))

# Contract type vs churn
query2 = """
SELECT 
    Contract,
    SUM(Churn) AS churned,
    COUNT(*) AS total,
    ROUND(100.0 * SUM(Churn) / COUNT(*), 1) AS churn_rate_pct
FROM customers
GROUP BY Contract
ORDER BY churn_rate_pct DESC
"""
print(pd.read_sql(query2, conn))

conn.close()

