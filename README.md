# Customer Churn Prediction Pipeline

An end-to-end data pipeline that predicts customer churn 
using Python, SQL, and AWS S3.

## Tech Stack
- Python (pandas, scikit-learn, boto3)
- SQL (SQLite / AWS Athena compatible)
- AWS S3 for data storage
- Logistic Regression model (~80% accuracy)

## Project Structure
```
customer-churn-pipeline/
├── data/           # Raw and processed data
├── scripts/        # Pipeline scripts
├── models/         # Saved ML model
└── tests/          # Unit tests (Week 2)
```

## How to Run
```bash
pip install -r requirements.txt
python scripts/upload_to_s3.py
python scripts/clean_data.py
python scripts/train_model.py
python scripts/predict_and_upload.py
```

## Results
- Model Accuracy: ~80%
- Dataset: IBM Telco Customer Churn (7,043 customers)

# Create requirements file
echo "pandas
boto3
scikit-learn
kaggle" > requirements.txt

# Push to GitHub
git init
git add .
git commit -m "Week 1: initial pipeline setup"
git branch -M main
git remote add origin https://github.com/yourusername/customer-churn-pipeline.git
git push -u origin main


# Customer Churn Prediction Pipeline

End-to-end data pipeline predicting telecom customer churn 
using Python, SQL, and AWS — built to mirror production 
data engineering practices.

## Stack
- Python (pandas, scikit-learn, boto3)
- SQL for customer segmentation analysis
- AWS S3 for data storage, AWS Lambda for automation
- GitHub Actions CI/CD with automated tests
- Logistic Regression model (~80% accuracy)

## Architecture
Raw CSV → S3 → Python ETL → Data Quality Checks 
→ ML Model → Predictions → S3 → Lambda Trigger → CI/CD

## Key Features
- Automated data quality validation (null checks, type checks)
- Pipeline monitoring with structured logging
- Automated test suite (pytest) with GitHub Actions CI/CD
- AWS Lambda for serverless pipeline triggering

## Results
- Rows processed: 7,043 customers
- Model accuracy: ~80%
- Churn rate in dataset: 26.5%

Built an end-to-end customer churn prediction pipeline using 
Python, SQL, and AWS (S3, Lambda) with automated data quality 
checks, pipeline monitoring, pytest test suite, and CI/CD via 
GitHub Actions — achieving ~80% model accuracy on 7,000+ 
customer records.

