import pandas as pd
import pickle
import boto3
import io

BUCKET_NAME = "churn-pipeline-aayushtiwari"

df = pd.read_csv("data/encoded_churn.csv")
X = df.drop(columns=["Churn"])

with open("models/churn_model.pkl", "rb") as f:
    model = pickle.load(f)

df["predicted_churn"] = model.predict(X)
df["churn_probability"] = model.predict_proba(X)[:, 1].round(3)

output_df = df[["predicted_churn", "churn_probability"]]

# Upload to S3
s3 = boto3.client("s3", region_name="eu-central-1")
csv_buffer = io.StringIO()
output_df.to_csv(csv_buffer, index=False)

s3.put_object(
    Bucket=BUCKET_NAME,
    Key="predictions/churn_predictions.csv",
    Body=csv_buffer.getvalue()
)
print("Predictions uploaded to S3!")