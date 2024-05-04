from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import requests
import pandas as pd

def get_data():
    response = requests.get("https://gist.githubusercontent.com/nadirbslmh/b50406d5579e875e6435896c9ff6c80c/raw/cac8007653b6145e9ad0ec69b1e4fd6c1be718e7/transactions.json")
    return response.json()

def perform_data_cleaning(**kwargs):
    data = kwargs['ti'].xcom_pull(task_ids='get_data_task')
    for transaction in data:
        transaction['phone_number'] = '+62' + transaction['phone_number']
        transaction['transaction_amount'] = 'Rp ' + '{:,.0f}'.format(transaction['transaction_amount']).replace(",", ".")
    success_transactions = [transaction for transaction in data if transaction['transaction_status'] == 'success']
    df = pd.DataFrame(success_transactions)
    df.to_csv('transaksi_clean.csv', index=False)

default_args = {
    'owner': 'ERISTA',
    'start_date': datetime(2024, 5, 4),
    'schedule_interval': '@daily'
}

with DAG('data_workflow', default_args=default_args, catchup=False) as dag:
    
    get_data_task = PythonOperator(
        task_id='get_data_task',
        python_callable=get_data
    )
    
    perform_data_cleaning_task = PythonOperator(
        task_id='perform_data_cleaning_task',
        python_callable=perform_data_cleaning,
        provide_context=True
    )
    
    get_data_task >> perform_data_cleaning_task