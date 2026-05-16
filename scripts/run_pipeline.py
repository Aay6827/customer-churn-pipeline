import logging
import os
import pandas as pd
from datetime import datetime
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import pickle
import boto3
import io

os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename=f"logs/pipeline_{datetime.now().strftime('%Y%m%d')}.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

BUCKET = "churn-pipeline-aayushtiwari"

def step1_load():
    logging.info("Step 1: Loading data")
    df = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")
    logging.info(f"Loaded {len(df)} rows")
    return df

def step2_clean(df):
    logging.info("Step 2: Cleaning data")
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce").fillna(0)
    df = df.drop(columns=["customerID"])
    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})
    cat_cols = df.select_dtypes(include="object").columns.tolist()
    le = LabelEncoder()
    for col in cat_cols:
        df[col] = le.fit_transform(df[col])
    logging.info("Cleaning done")
    return df

def step3_quality_check(df):
    logging.info("Step 3: Data quality checks")
    assert not df.empty, "Dataframe is empty!"
    assert df["Churn"].isnull().sum() == 0, "Nulls in Churn!"
    assert set(df["Churn"].unique()).issubset({0,1}), "Bad Churn values!"
    logging.info("Quality checks passed")

def step4_train(df):
    logging.info("Step 4: Training model")
    X = df.drop(columns=["Churn"])
    y = df["Churn"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    acc = accuracy_score(y_test, model.predict(X_test))
    logging.info(f"Model accuracy: {acc:.3f}")
    with open("models/churn_model.pkl", "wb") as f:
        pickle.dump(model, f)
    return model
def step5_upload(df, model):
    logging.info("Step 5: Uploading predictions to S3")
    X = df.drop(columns=["Churn"])
    df["predicted_churn"] = model.predict(X)
    s3 = boto3.client("s3", region_name="eu-central-1")
    buf = io.StringIO()
    df[["predicted_churn"]].to_csv(buf, index=False)
    s3.put_object(Bucket=BUCKET, Key="predictions/churn_predictions.csv", Body=buf.getvalue())
    logging.info("Upload complete")

if __name__ == "__main__":
    df = step1_load()
    df = step2_clean(df)
    step3_quality_check(df)
    model = step4_train(df)
    step5_upload(df, model)
    print("Pipeline complete! Check logs/pipeline_*.log for details.")
    