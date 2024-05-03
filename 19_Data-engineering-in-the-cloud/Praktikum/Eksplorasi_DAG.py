from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import requests
import pandas as pd
import firebase_admin
from firebase_admin import credentials, storage
import pyarrow.parquet as pq
import pyarrow as pa

cred = credentials.Certificate("keyErista.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'erista-cloud.appspot.com'
})

default_args = {
    'owner': 'ERISTA',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

def get_data():
    response = requests.get('https://fakestoreapi.com/products')
    return response.json()

def transform_product_data(**kwargs):
    task_instance = kwargs['ti']
    data = task_instance.xcom_pull(task_ids='get_data')
    transformed_data = []
    for product in data:
        if product['price'] > 100:
            transformed_product = {
                'title': product['title'],
                'price': product['price'],
                'description': product['description'],
                'category': product['category']
            }
            transformed_data.append(transformed_product)
    return transformed_data

def save_as_parquet_file(**kwargs):
    task_instance = kwargs['ti']
    transformed_data = task_instance.xcom_pull(task_ids='transform_data')
    df = pd.DataFrame(transformed_data)
    pq.write_table(pa.Table.from_pandas(df), 'data_transform.parquet')

def upload_to_firebase_storage():
    bucket_name = 'erista-cloud.appspot.com'
    blob = storage.bucket(bucket_name).blob('data_transform.parquet')
    blob.upload_from_filename('data_transform.parquet')

with DAG('19_DAG_EKS',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    get_data_task = PythonOperator(
        task_id='get_data',
        python_callable=get_data
    )

    transform_data_task = PythonOperator(
        task_id='transform_data',
        python_callable=transform_product_data,
        provide_context=True
    )

    save_as_parquet_task = PythonOperator(
        task_id='save_as_parquet_file',
        python_callable=save_as_parquet_file,
        provide_context=True
    )

    upload_to_firebase_task = PythonOperator(
        task_id='upload_to_firebase_storage',
        python_callable=upload_to_firebase_storage
    )

    get_data_task >> transform_data_task >> save_as_parquet_task >> upload_to_firebase_task