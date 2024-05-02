from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime, timedelta
import requests
import logging

default_args = {
    'owner': 'ERISTA',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 23),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    '17_dag_buah',
    default_args=default_args,
    description='DAG sederhana untuk mengambil dan menyimpan data buah dari API',
    schedule_interval=timedelta(days=1),
)

def tambah_data_buah_ke_db(**kwargs):
    data_buah = kwargs['ti'].xcom_pull(task_ids='dapatkan_data_buah')
    hook = PostgresHook(postgres_conn_id='postgres_default')
    koneksi = hook.get_conn()
    kursor = koneksi.cursor()

    for buah in data_buah:
        kursor.execute('''
            INSERT INTO buah (name, calories, fat, sugar, carbohydrates, protein)
            VALUES (%s, %s, %s, %s, %s, %s);
        ''', (
            buah['name'],
            buah['nutritions']['calories'],
            buah['nutritions']['fat'],
            buah['nutritions']['sugar'],
            buah['nutritions']['carbohydrates'],
            buah['nutritions']['protein'],
        ))

    koneksi.commit()
    kursor.close()

create_buah_table = PostgresOperator(
    task_id='create_buah_table',
    postgres_conn_id='postgres_default',
    sql="""
        CREATE TABLE IF NOT EXISTS buah (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            calories DECIMAL NOT NULL,
            fat DECIMAL NOT NULL,
            sugar DECIMAL NOT NULL,
            carbohydrates DECIMAL NOT NULL,
            protein DECIMAL NOT NULL
        );
    """,
    dag=dag,
)

def dapatkan_data_api():
    try:
        respons = requests.get("https://www.fruityvice.com/api/fruit/family/Rosaceae")
        respons.raise_for_status()
        return respons.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Gagal mengambil data dari API: {e}")
        raise

dapatkan_data_buah = PythonOperator(
    task_id='dapatkan_data_buah',
    python_callable=dapatkan_data_api,
    dag=dag,
)

tambah_data_buah = PythonOperator(
    task_id='tambah_data_buah',
    python_callable=tambah_data_buah_ke_db,
    provide_context=True,
    dag=dag,
)

create_buah_table >> dapatkan_data_buah >> tambah_data_buah