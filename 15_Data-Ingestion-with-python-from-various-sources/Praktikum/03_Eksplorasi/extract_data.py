from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import requests
import pandas as pd
import os

default_args = {
    'owner': 'hikmal',
    "retries" : 2,
    "retry_delay" : timedelta(minutes=2),
    'start_date': datetime(2024, 4, 1),
    'schedule_interval': '0 9 * * 1'  # Setiap minggu pada hari Senin jam 09:00
}

def extract_data():
    url = "https://gist.githubusercontent.com/nadirbslmh/8922f71875948802321ef479a017f4c0/raw/1fbbc4b3d55f8ae717eb197d9aaf530ed1bc7ed2/sample.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('data', [])
    else:
        print("Failed to fetch data from the API")
        return []

def save_to_csv(data):
    df = pd.DataFrame(data)
    airflow_data_folder = os.path.expanduser('~/airflow/data')
    if not os.path.exists(airflow_data_folder):
        os.makedirs(airflow_data_folder)
    filepath = os.path.join(airflow_data_folder, 'books_data.csv')
    df.to_csv(filepath, index=False)

with DAG(
    'book_extraction_dag', 
    default_args=default_args, 
    description='extract book data', 
    catchup=False
) as dag:
    extract_task = PythonOperator(
        task_id='extract_task',
        python_callable=extract_data
    )

    save_csv_task = PythonOperator(
        task_id='save_csv_task',
        python_callable=save_to_csv,
        op_args=[extract_task.output]  # Menggunakan output dari extract_task sebagai argumen
    )

extract_task >> save_csv_task
