import logging
import pandas as pd
from datetime import datetime

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

import os
os.makedirs("logs", exist_ok=True)

def monitor_pipeline(filepath):
    try:
        df = pd.read_csv(filepath)
        row_count = len(df)
        churn_rate = df["Churn"].mean().round(3)
        
        logging.info(f"Pipeline run: {datetime.now()}")
        logging.info(f"Rows processed: {row_count}")
        logging.info(f"Churn rate: {churn_rate * 100:.1f}%")
        
        if row_count < 1000:
            logging.warning(f"Low row count: {row_count}")
            
        print(f"Monitored: {row_count} rows, churn rate {churn_rate*100:.1f}%")
        
    except Exception as e:
        logging.error(f"Pipeline failed: {str(e)}")
        raise e

monitor_pipeline("data/cleaned_churn.csv")

