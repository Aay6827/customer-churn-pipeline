import boto3

BUCKET_NAME = "churn-pipeline-aayushtiwari "   # replace with your bucket
FILE_PATH = "data/WA_Fn-UseC_-Telco-Customer-Churn.csv"
S3_KEY = "raw/telco_churn.csv"

s3 = boto3.client("s3", region_name="eu-central-1")

s3.upload_file(FILE_PATH, BUCKET_NAME, S3_KEY)
print(f"Uploaded {FILE_PATH} to s3://{BUCKET_NAME}/{S3_KEY}")
