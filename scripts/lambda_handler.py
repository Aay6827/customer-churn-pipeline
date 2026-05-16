import boto3
import pandas as pd
import pickle
import io
import json

def lambda_handler(event, context):
    BUCKET = "your-bucket-name"
    s3 = boto3.client("s3")
    
    # Download cleaned data from S3
    obj = s3.get_object(Bucket=BUCKET, Key="raw/telco_churn.csv")
    df = pd.read_csv(io.BytesIO(obj["Body"].read()))
    
    # Basic cleaning
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce").fillna(0)
    df = df.drop(columns=["customerID"])
    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})
    
    row_count = len(df)
    churn_rate = df["Churn"].mean()
    
    # Upload result summary
    summary = {
        "rows_processed": row_count,
        "churn_rate": round(float(churn_rate), 3),
        "status": "success"
    }
    
    s3.put_object(
        Bucket=BUCKET,
        Key="logs/pipeline_summary.json",
        Body=json.dumps(summary)
    )
    
    return {
        "statusCode": 200,
        "body": json.dumps(summary)
    }

