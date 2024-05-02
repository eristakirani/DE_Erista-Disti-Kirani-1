from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
import requests
import pandas as pd
import os
import logging

default_args = {
    'owner': 'ERISTA',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

OUTPUT_DIR = 'C:'

def fetch_and_store_data(endpoint, output_file):
    try:
        response = requests.get(endpoint)
        response.raise_for_status()
        data = response.json()
        
        # Write data to CSV
        df = pd.json_normalize(data)
        df.to_csv(output_file + ".csv", index=False)
        
        # Write titles to TXT
        with open(output_file + ".txt", "w") as txt_file:
            for item in data:
                txt_file.write(f"{item['title']}\n")

        logging.info(f"Data written to files: {output_file}.csv and {output_file}.txt")
    except Exception as e:
        logging.error(f"Failed to fetch and store data: {e}")
        raise

dag = DAG(
    'simple_api_dag',
    default_args=default_args,
    description='Simple DAG for fetching data from API',
    schedule_interval=None,
    start_date=datetime(2024, 4, 20)
)

fetch_and_store_task = PythonOperator(
    task_id='fetch_and_store_data',
    python_callable=fetch_and_store_data,
    op_kwargs={
        'endpoint': "https://fakestoreapi.com/products",
        'output_file': os.path.join(OUTPUT_DIR, "data")
    },
    dag=dag,
)

fetch_and_store_task